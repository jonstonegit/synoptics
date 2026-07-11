"""Validation utilities for pathology synoptic definitions.

This module deliberately has no Streamlit dependency. It validates the
configuration dictionaries used to build widgets and the tuples used to
render the finished report.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .errors import SynopticConfigurationError


SUPPORTED_FIELD_TYPES = frozenset(
    {
        "radio",
        "radio_other",
        "conditional_radio",
        "conditional_radio_other",
        "conditional_radio_multiple",
        "checkbox_group",
        "text",
        "textarea",
        "radio_toggle",
        "option_toggle",
        "conditional_value",
    }
)

ROW_LENGTHS = {
    "title": 3,
    "section": 2,
    "row": 3,
    "indent": 3,
}


def require_key(field: Mapping[str, Any], key: str, context: str) -> Any:
    """Return a required value or raise a descriptive configuration error."""
    if key not in field:
        raise SynopticConfigurationError(
            f"{context} is missing required key {key!r}."
        )

    return field[key]


def validate_nonempty_string(value: Any, name: str, context: str) -> None:
    """Require a non-empty string."""
    if not isinstance(value, str) or not value.strip():
        raise SynopticConfigurationError(
            f"{context}: {name} must be a non-empty string; "
            f"received {value!r}."
        )


def validate_options(
    options: Any,
    name: str,
    context: str,
) -> None:
    """Validate a non-empty sequence of unique, non-empty strings."""
    if (
        not isinstance(options, Sequence)
        or isinstance(options, (str, bytes))
        or not options
    ):
        raise SynopticConfigurationError(
            f"{context}: {name} must be a non-empty list or tuple."
        )

    for index, option in enumerate(options):
        if not isinstance(option, str) or not option.strip():
            raise SynopticConfigurationError(
                f"{context}: {name}[{index}] must be a non-empty string; "
                f"received {option!r}."
            )

    if len(set(options)) != len(options):
        raise SynopticConfigurationError(
            f"{context}: {name} contains duplicate options."
        )


def validate_children(children: Any, context: str) -> None:
    """Validate one child field or a non-empty sequence of child fields."""
    if isinstance(children, Mapping):
        child_fields = [children]
    elif (
        isinstance(children, Sequence)
        and not isinstance(children, (str, bytes))
        and children
    ):
        child_fields = children
    else:
        raise SynopticConfigurationError(
            f"{context} must be a field dictionary or a non-empty "
            "list or tuple of field dictionaries."
        )

    for index, child in enumerate(child_fields):
        validate_field(child, f"{context}[{index}]")


def _validate_conditional_field_mapping(
    conditional_fields: Any,
    options: Sequence[str],
    context: str,
) -> None:
    """Validate a mapping from selectable options to child field definitions."""
    if not isinstance(conditional_fields, Mapping):
        raise SynopticConfigurationError(
            f"{context}: conditional_fields must be a dictionary."
        )

    allowed_options = set(options)
    unknown_options = set(conditional_fields) - allowed_options

    if unknown_options:
        raise SynopticConfigurationError(
            f"{context}: conditional_fields contains unknown option(s): "
            f"{sorted(unknown_options)}."
        )

    for option, children in conditional_fields.items():
        validate_children(
            children,
            f"{context}.conditional_fields[{option!r}]",
        )


def validate_field(field: Any, context: str = "field") -> None:
    """Validate one field definition, including any nested child fields."""
    if not isinstance(field, Mapping):
        raise SynopticConfigurationError(
            f"{context} must be a dictionary, not {type(field).__name__}."
        )

    label = require_key(field, "label", context)
    field_type = require_key(field, "type", context)

    validate_nonempty_string(label, "label", context)
    validate_nonempty_string(field_type, "type", context)

    field_context = f"{context} ({label!r})"

    if field_type not in SUPPORTED_FIELD_TYPES:
        raise SynopticConfigurationError(
            f"{field_context}: unsupported field type {field_type!r}. "
            f"Supported types: {', '.join(sorted(SUPPORTED_FIELD_TYPES))}."
        )

    if "key" in field:
        validate_nonempty_string(field["key"], "key", field_context)

    option_field_types = {
        "radio",
        "radio_other",
        "conditional_radio",
        "conditional_radio_other",
        "conditional_radio_multiple",
        "checkbox_group",
        "conditional_value",
    }

    if field_type in option_field_types:
        options = require_key(field, "options", field_context)
        validate_options(options, "options", field_context)

    if field_type in {"radio_other", "conditional_radio_other"}:
        if "Other" in field["options"]:
            raise SynopticConfigurationError(
                f"{field_context}: do not include 'Other' in options; "
                "the widget adds it automatically."
            )

    if field_type in {"conditional_radio", "conditional_radio_other"}:
        trigger = require_key(field, "trigger", field_context)
        sublabel = require_key(field, "sublabel", field_context)
        suboptions = require_key(field, "suboptions", field_context)

        validate_nonempty_string(trigger, "trigger", field_context)
        validate_nonempty_string(sublabel, "sublabel", field_context)
        validate_options(suboptions, "suboptions", field_context)

        if trigger not in field["options"]:
            raise SynopticConfigurationError(
                f"{field_context}: trigger {trigger!r} is not present "
                "in options."
            )

    if field_type == "conditional_radio_multiple":
        conditional_fields = require_key(
            field,
            "conditional_fields",
            field_context,
        )
        _validate_conditional_field_mapping(
            conditional_fields,
            field["options"],
            field_context,
        )

        allow_other = field.get("allow_other", False)
        if not isinstance(allow_other, bool):
            raise SynopticConfigurationError(
                f"{field_context}: allow_other must be True or False."
            )

        if allow_other and "Other" in field["options"]:
            raise SynopticConfigurationError(
                f"{field_context}: do not include 'Other' in options when "
                "allow_other=True; the widget adds it automatically."
            )

    if field_type == "checkbox_group":
        conditional_fields = require_key(
            field,
            "conditional_fields",
            field_context,
        )
        _validate_conditional_field_mapping(
            conditional_fields,
            field["options"],
            field_context,
        )

        comment = field.get("comment", False)
        if not isinstance(comment, bool):
            raise SynopticConfigurationError(
                f"{field_context}: comment must be True or False."
            )

        allowed_options = set(field["options"])
        default = field.get("default")

        if default is not None and default not in allowed_options:
            raise SynopticConfigurationError(
                f"{field_context}: default {default!r} is not present "
                "in options."
            )

        exclusive_options = field.get("exclusive_options", [])
        validate_options_or_empty(
            exclusive_options,
            "exclusive_options",
            field_context,
        )

        unknown_exclusive = set(exclusive_options) - allowed_options
        if unknown_exclusive:
            raise SynopticConfigurationError(
                f"{field_context}: exclusive_options contains unknown "
                f"option(s): {sorted(unknown_exclusive)}."
            )

    if field_type == "text":
        suffix = field.get("suffix", "")
        if not isinstance(suffix, str):
            raise SynopticConfigurationError(
                f"{field_context}: suffix must be a string."
            )

    if field_type == "radio_toggle":
        options = require_key(field, "options", field_context)
        session_key = require_key(field, "session_key", field_context)

        validate_nonempty_string(
            session_key,
            "session_key",
            field_context,
        )

        if (
            not isinstance(options, Sequence)
            or isinstance(options, (str, bytes))
            or not options
        ):
            raise SynopticConfigurationError(
                f"{field_context}: options must contain at least one "
                "(display_text, short_text) pair."
            )

        display_values: list[str] = []

        for index, option in enumerate(options):
            if (
                not isinstance(option, Sequence)
                or isinstance(option, (str, bytes))
                or len(option) != 2
            ):
                raise SynopticConfigurationError(
                    f"{field_context}: options[{index}] must be a "
                    "(display_text, short_text) pair."
                )

            display_text, short_text = option
            validate_nonempty_string(
                display_text,
                f"options[{index}] display text",
                field_context,
            )
            validate_nonempty_string(
                short_text,
                f"options[{index}] short text",
                field_context,
            )
            display_values.append(display_text)

        if len(set(display_values)) != len(display_values):
            raise SynopticConfigurationError(
                f"{field_context}: radio-toggle display text must be unique."
            )

    if field_type == "option_toggle":
        key = require_key(field, "key", field_context)
        validate_nonempty_string(key, "key", field_context)

        default = field.get("default", False)
        if not isinstance(default, bool):
            raise SynopticConfigurationError(
                f"{field_context}: default must be True or False."
            )

    if field_type == "conditional_value":
        value_fields = require_key(field, "value_fields", field_context)

        if not isinstance(value_fields, Mapping):
            raise SynopticConfigurationError(
                f"{field_context}: value_fields must be a dictionary."
            )

        unknown_options = set(value_fields) - set(field["options"])
        if unknown_options:
            raise SynopticConfigurationError(
                f"{field_context}: value_fields contains unknown option(s): "
                f"{sorted(unknown_options)}."
            )

        for option, configuration in value_fields.items():
            if (
                not isinstance(configuration, Sequence)
                or isinstance(configuration, (str, bytes))
                or len(configuration) != 2
            ):
                raise SynopticConfigurationError(
                    f"{field_context}: value_fields[{option!r}] must be a "
                    "(prompt, suffix) pair."
                )

            prompt, suffix = configuration
            validate_nonempty_string(
                prompt,
                f"value_fields[{option!r}] prompt",
                field_context,
            )

            if not isinstance(suffix, str):
                raise SynopticConfigurationError(
                    f"{field_context}: suffix for {option!r} must be a string."
                )


def validate_options_or_empty(
    options: Any,
    name: str,
    context: str,
) -> None:
    """Validate an empty or non-empty list/tuple of unique strings."""
    if not isinstance(options, Sequence) or isinstance(options, (str, bytes)):
        raise SynopticConfigurationError(
            f"{context}: {name} must be a list or tuple."
        )

    if not options:
        return

    validate_options(options, name, context)


def validate_output_row(row: Any, index: int | None = None) -> None:
    """Validate one report-output tuple."""
    context = "output row" if index is None else f"output row {index}"

    if not isinstance(row, tuple):
        raise SynopticConfigurationError(
            f"{context} must be a tuple, not {type(row).__name__}."
        )

    if not row:
        raise SynopticConfigurationError(f"{context} cannot be empty.")

    row_type = row[0]
    if row_type not in ROW_LENGTHS:
        raise SynopticConfigurationError(
            f"{context} has unsupported row type {row_type!r}. "
            f"Supported row types: {', '.join(ROW_LENGTHS)}."
        )

    expected_length = ROW_LENGTHS[row_type]
    if len(row) != expected_length:
        raise SynopticConfigurationError(
            f"{context} of type {row_type!r} must have "
            f"{expected_length} items; received {len(row)}."
        )

    validate_nonempty_string(row[1], "row label", context)

    if row_type == "title":
        validate_nonempty_string(row[2], "title value", context)


def validate_rows(rows: Any) -> None:
    """Validate a collection of generated report rows."""
    if (
        not isinstance(rows, Sequence)
        or isinstance(rows, (str, bytes))
    ):
        raise SynopticConfigurationError(
            f"rows must be a list or tuple, not {type(rows).__name__}."
        )

    for index, row in enumerate(rows):
        validate_output_row(row, index)


def validate_synoptic(synoptic: Any) -> None:
    """Validate a complete synoptic definition before rendering it."""
    if (
        not isinstance(synoptic, Sequence)
        or isinstance(synoptic, (str, bytes))
    ):
        raise SynopticConfigurationError(
            "A synoptic must be a list or tuple containing field "
            "dictionaries and/or output-row tuples."
        )

    if not synoptic:
        raise SynopticConfigurationError("A synoptic cannot be empty.")

    for index, item in enumerate(synoptic):
        context = f"synoptic item {index}"

        if isinstance(item, tuple):
            validate_output_row(item, index)
        elif isinstance(item, Mapping):
            validate_field(item, context)
        else:
            raise SynopticConfigurationError(
                f"{context} must be a field dictionary or output-row tuple, "
                f"not {type(item).__name__}."
            )


__all__ = [
    "ROW_LENGTHS",
    "SUPPORTED_FIELD_TYPES",
    "require_key",
    "validate_children",
    "validate_field",
    "validate_nonempty_string",
    "validate_options",
    "validate_options_or_empty",
    "validate_output_row",
    "validate_rows",
    "validate_synoptic",
]
