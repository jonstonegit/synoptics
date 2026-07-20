"""Factory functions for pathology synoptic field definitions.

Each function creates one field-definition dictionary and validates it
immediately. This allows malformed CAP synoptic fields to fail when their
data module is imported rather than later during Streamlit rendering.
"""

from __future__ import annotations

from typing import Any

from .validation import validate_field


def _validated(field: dict[str, Any]) -> dict[str, Any]:
    """Validate and return a completed field-definition dictionary."""
    validate_field(field)
    return field


def radio(
    label: str,
    options: list[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Create a single-choice radio field."""
    return _validated(
        {
            "type": "radio",
            "label": label,
            "options": options,
            "key": key or label,
        }
    )


def radio_other(
    label: str,
    options: list[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Create a radio field that automatically includes an Other choice."""
    return _validated(
        {
            "type": "radio_other",
            "label": label,
            "options": options,
            "key": key or label,
        }
    )


def text(
    label: str,
    suffix: str = "",
    key: str | None = None,
) -> dict[str, Any]:
    """Create a single-line text-entry field."""
    return _validated(
        {
            "type": "text",
            "label": label,
            "suffix": suffix,
            "key": key or label,
        }
    )


def textarea(
    label: str,
    key: str | None = None,
) -> dict[str, Any]:
    """Create a multiline text-entry field."""
    return _validated(
        {
            "type": "textarea",
            "label": label,
            "key": key or label,
        }
    )


def conditional_radio(
    label: str,
    options: list[str],
    trigger: str,
    sublabel: str,
    suboptions: list[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Create a radio field that reveals a select box for one answer."""
    return _validated(
        {
            "type": "conditional_radio",
            "label": label,
            "options": options,
            "trigger": trigger,
            "sublabel": sublabel,
            "suboptions": suboptions,
            "key": key or label,
        }
    )


def conditional_radio_other(
    label: str,
    options: list[str],
    trigger: str,
    sublabel: str,
    suboptions: list[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Create a conditional radio field that also permits free text."""
    return _validated(
        {
            "type": "conditional_radio_other",
            "label": label,
            "options": options,
            "trigger": trigger,
            "sublabel": sublabel,
            "suboptions": suboptions,
            "key": key or label,
        }
    )


def conditional_radio_multiple(
    label: str,
    options: list[str],
    conditional_fields: dict[
        str,
        dict[str, Any] | list[dict[str, Any]],
    ],
    allow_other: bool = False,
    child_value_options: list[str] | None = None,
    default: str | None = None,
    key: str | None = None,
) -> dict[str, Any]:
    """Create a radio field whose answer can reveal child fields."""

    return _validated(
        {
            "type": "conditional_radio_multiple",
            "label": label,
            "options": options,
            "conditional_fields": conditional_fields,
            "allow_other": allow_other,
            "child_value_options": child_value_options or [],
            "default": default,
            "key": key or label,
        }
    )


def checkbox_group(
    label: str,
    options: list[str],
    conditional_fields: (
        dict[str, dict[str, Any] | list[dict[str, Any]]] | None
    ) = None,
    comment: bool = False,
    default: str | None = None,
    exclusive_options: list[str] | None = None,
    key: str | None = None,
) -> dict[str, Any]:
    """Create a multiple-choice checkbox group with optional child fields."""
    return _validated(
        {
            "type": "checkbox_group",
            "label": label,
            "options": options,
            "conditional_fields": conditional_fields or {},
            "comment": comment,
            "default": default,
            "exclusive_options": exclusive_options or [],
            "key": key or label,
        }
    )


def conditional_value(
    label: str,
    options: list[str],
    value_fields: dict[str, tuple[str, str]],
    key: str | None = None,
) -> dict[str, Any]:
    """Create a choice field whose answers may request a typed value."""
    return _validated(
        {
            "type": "conditional_value",
            "label": label,
            "options": options,
            "value_fields": value_fields,
            "key": key or label,
        }
    )


def radio_toggle(
    label: str,
    options: list[tuple[str, str]],
    session_key: str,
    key: str | None = None,
) -> dict[str, Any]:
    """Create a radio field with long and abbreviated output values."""
    return _validated(
        {
            "type": "radio_toggle",
            "label": label,
            "options": options,
            "session_key": session_key,
            "key": key or f"{label}_radio",
        }
    )


def option_toggle(
    label: str,
    key: str,
    default: bool = False,
) -> dict[str, Any]:
    """Create a checkbox that controls a report-display option."""
    return _validated(
        {
            "type": "option_toggle",
            "label": label,
            "key": key,
            "default": default,
        }
    )

def display_link(
    label: str,
    url: str,
    link_text: str,
) -> dict[str, Any]:
    """Create a clickable link that is not included in the report."""

    return _validated(
        {
            "type": "display_link",
            "label": label,
            "url": url,
            "link_text": link_text,
        }
    )

def text_group(
    label: str,
    child_fields: dict[str, Any] | list[dict[str, Any]],
    prompt: str = "Tumor Identifier",
    key: str | None = None,
) -> dict[str, Any]:
    """Create a text field with nested child fields."""

    return _validated(
        {
            "type": "text_group",
            "label": label,
            "prompt": prompt,
            "child_fields": child_fields,
            "key": key or label,
        }
    )


__all__ = [
    "checkbox_group",
    "conditional_radio",
    "conditional_radio_multiple",
    "conditional_radio_other",
    "conditional_value",
    "display_link",
    "option_toggle",
    "radio",
    "radio_other",
    "radio_toggle",
    "text",
    "textarea",
    "text_group",
    
]

