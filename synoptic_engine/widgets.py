"""Streamlit widget rendering for pathology synoptic fields."""

from __future__ import annotations

import html
from collections.abc import Mapping, Sequence
from typing import Any

import streamlit as st

from .errors import SynopticConfigurationError
from .validation import validate_field


OutputRow = tuple[Any, ...]
FieldResult = tuple[str, Any, list[OutputRow]]


def field_label(label: str) -> None:
    """Render a consistent bold label above a Streamlit widget."""
    if not isinstance(label, str) or not label.strip():
        raise SynopticConfigurationError(
            f"Field label must be a non-empty string; received {label!r}."
        )

    st.markdown(
        f"""
        <div style="
            font-size:16px;
            font-weight:bold;
            margin-top:10px;
            margin-bottom:4px;
        ">
            {html.escape(label)}
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_field_value(
    field: dict[str, Any],
    indent_level: int = 0,
) -> FieldResult:
    """Render one field and return its label, value, and child rows."""
    validate_field(field)

    if not isinstance(indent_level, int) or indent_level < 0:
        raise ValueError("indent_level must be a non-negative integer.")

    if indent_level == 0:
        return _get_field_value(field, indent_level)

    indent_width = min(indent_level * 0.03, 0.15)

    _, content_column = st.columns(
        [indent_width, 1 - indent_width]
    )

    with content_column:
        return _get_field_value(field, indent_level)


def _normalize_children(
    configured_children: Any,
    *,
    context: str,
) -> list[dict[str, Any]]:
    """Return one child dictionary or a sequence of children as a list."""
    if isinstance(configured_children, Mapping):
        children = [dict(configured_children)]
    elif (
        isinstance(configured_children, Sequence)
        and not isinstance(configured_children, (str, bytes))
    ):
        children = list(configured_children)
    else:
        raise SynopticConfigurationError(
            f"{context} must be a field dictionary or a list of "
            "field dictionaries."
        )

    if not children:
        raise SynopticConfigurationError(
            f"{context} cannot be empty."
        )

    for index, child in enumerate(children):
        if not isinstance(child, Mapping):
            raise SynopticConfigurationError(
                f"{context}[{index}] must be a field dictionary, not "
                f"{type(child).__name__}."
            )

        validate_field(child, f"{context}[{index}]")

    return [dict(child) for child in children]


def _render_children(
    configured_children: Any,
    *,
    indent_level: int,
    context: str,
) -> list[OutputRow]:
    """Render nested fields and convert them to indented output rows."""
    child_rows: list[OutputRow] = []

    for child_field in _normalize_children(
        configured_children,
        context=context,
    ):
        child_label, child_value, child_children = get_field_value(
            child_field,
            indent_level + 1,
        )

        child_rows.append(
            ("indent", child_label, child_value)
        )
        child_rows.extend(child_children)

    return child_rows


def _get_field_value(
    field: dict[str, Any],
    indent_level: int,
) -> FieldResult:
    """Render a validated field definition."""
    label = field["label"]
    field_type = field["type"]
    base_key = field.get("key", label)

    if field_type == "radio":
        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=base_key,
            label_visibility="collapsed",
        )

        return label, value, []

    if field_type == "radio_other":
        field_label(label)

        value = st.radio(
            "",
            [*field["options"], "Other"],
            key=base_key,
            label_visibility="collapsed",
        )

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{base_key}_other",
            )

        return label, value, []

    if field_type == "conditional_radio":
        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=base_key,
            label_visibility="collapsed",
        )

        child_rows: list[OutputRow] = []

        if value == field["trigger"]:
            subvalue = st.selectbox(
                field["sublabel"],
                field["suboptions"],
                key=f"{base_key}_{field['sublabel']}",
            )

            child_rows.append(
                (
                    "indent",
                    field["sublabel"],
                    subvalue,
                )
            )

        return label, value, child_rows

    if field_type == "conditional_radio_other":
        field_label(label)

        value = st.radio(
            "",
            [*field["options"], "Other"],
            key=base_key,
            label_visibility="collapsed",
        )

        child_rows: list[OutputRow] = []

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{base_key}_other",
            )
            return label, value, child_rows

        if value == field["trigger"]:
            subvalue = st.selectbox(
                field["sublabel"],
                field["suboptions"],
                key=f"{base_key}_{field['sublabel']}",
            )

            child_rows.append(
                (
                    "indent",
                    field["sublabel"],
                    subvalue,
                )
            )

        return label, value, child_rows

    if field_type == "text":
        value = st.text_input(
            f"Specify {label}",
            key=base_key,
        )

        suffix = field.get("suffix", "")

        if value:
            value = f"{value}{suffix}"

        return label, value, []

    if field_type == "textarea":
        value = st.text_area(
            label,
            key=base_key,
        )

        return label, value, []

    if field_type == "conditional_radio_multiple":
        field_label(label)

        options = list(field["options"])

        if field.get("allow_other", False):
            options.append("Other")

        value = st.radio(
            "",
            options,
            key=base_key,
            label_visibility="collapsed",
        )

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{base_key}_other",
            )
            return label, value, []

        child_rows: list[OutputRow] = []
        conditional_fields = field["conditional_fields"]

        if value in conditional_fields:
            child_rows.extend(
                _render_children(
                    conditional_fields[value],
                    indent_level=indent_level,
                    context=(
                        f"Field {label!r} conditional_fields[{value!r}]"
                    ),
                )
            )

        return label, value, child_rows

    if field_type == "checkbox_group":
        selected_values: list[str] = []
        child_rows: list[OutputRow] = []

        field_label(label)

        exclusive_options = field.get("exclusive_options", [])

        option_keys = {
            option: f"{base_key}_{option}"
            for option in field["options"]
        }

        default_option = field.get("default")

        for option, option_key in option_keys.items():
            if option_key not in st.session_state:
                st.session_state[option_key] = option == default_option

        for option in field["options"]:
            option_key = option_keys[option]

            is_checked = st.checkbox(
                option,
                key=option_key,
                on_change=handle_exclusive_checkbox,
                args=(
                    option_key,
                    option_keys,
                    exclusive_options,
                ),
            )

            if not is_checked:
                continue

            selected_values.append(option)

            conditional_fields = field["conditional_fields"]

            if option in conditional_fields:
                child_rows.extend(
                    _render_children(
                        conditional_fields[option],
                        indent_level=indent_level,
                        context=(
                            f"Field {label!r} "
                            f"conditional_fields[{option!r}]"
                        ),
                    )
                )

        if field.get("comment", False) and selected_values:
            comment = st.text_input(
                f"{label} Comment",
                key=f"{base_key}_comment",
            )

            if comment:
                child_rows.append(
                    ("indent", "Comment", comment)
                )

        value = "; ".join(selected_values)

        return label, value, child_rows

    if field_type == "radio_toggle":
        field_label(label)

        display_options = [
            full_text
            for full_text, _ in field["options"]
        ]

        selected_display = st.radio(
            "",
            display_options,
            key=base_key,
            label_visibility="collapsed",
        )

        matching_options = [
            short_text
            for full_text, short_text in field["options"]
            if full_text == selected_display
        ]

        if len(matching_options) != 1:
            raise SynopticConfigurationError(
                f"Field {label!r} could not map selected display value "
                f"{selected_display!r} to exactly one short value."
            )

        selected_short = matching_options[0]

        show_full = st.session_state.get(
            field["session_key"],
            False,
        )

        value = selected_display if show_full else selected_short

        return label, value, []

    if field_type == "option_toggle":
        st.markdown(
            (
                "<span style='font-size:18px; font-weight:bold;'>"
                "Table Options</span>"
            ),
            unsafe_allow_html=True,
        )

        st.checkbox(
            label,
            value=field.get("default", False),
            key=base_key,
        )

        return label, "", []

    if field_type == "conditional_value":
        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=base_key,
            label_visibility="collapsed",
        )

        if value == "Not applicable":
            return label, "", []

        value_fields = field["value_fields"]

        if value in value_fields:
            prompt, suffix = value_fields[value]

            entered = st.text_input(
                prompt,
                key=f"{base_key}_{value}",
            )

            if entered:
                entered = f"{entered}{suffix}" if suffix else entered

                if value in {
                    "Exact size",
                    "Exact number",
                    "Exact distance in cm",
                    "Exact distance in mm",
                }:
                    return label, entered, []

                if value == "At least":
                    return label, f"At least {entered}", []

                if value in {
                    "Other",
                    "Cannot be determined",
                }:
                    return (
                        label,
                        value,
                        [("indent", "Comment", entered)],
                    )

        return label, value, []

    raise SynopticConfigurationError(
        f"Unsupported field type {field_type!r} for field {label!r}."
    )


def handle_exclusive_checkbox(
    changed_key: str,
    option_keys: dict[str, str],
    exclusive_options: list[str],
) -> None:
    """Enforce mutually exclusive choices within a checkbox group."""
    if not isinstance(changed_key, str) or not changed_key:
        raise SynopticConfigurationError(
            "changed_key must be a non-empty string."
        )

    if changed_key not in option_keys.values():
        raise SynopticConfigurationError(
            f"Checkbox key {changed_key!r} is not present in option_keys."
        )

    unknown_exclusive = set(exclusive_options) - set(option_keys)

    if unknown_exclusive:
        raise SynopticConfigurationError(
            "exclusive_options contains unknown option(s): "
            f"{sorted(unknown_exclusive)}."
        )

    if not st.session_state.get(changed_key, False):
        return

    changed_option = next(
        option
        for option, key in option_keys.items()
        if key == changed_key
    )

    if changed_option in exclusive_options:
        for option, key in option_keys.items():
            if option != changed_option:
                st.session_state[key] = False
    else:
        for exclusive_option in exclusive_options:
            exclusive_key = option_keys[exclusive_option]
            st.session_state[exclusive_key] = False


__all__ = [
    "FieldResult",
    "OutputRow",
    "field_label",
    "get_field_value",
    "handle_exclusive_checkbox",
]
