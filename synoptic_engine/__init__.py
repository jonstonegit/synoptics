"""Public interface for the synoptic engine."""

from .definitions import (
    checkbox_group,
    conditional_radio,
    conditional_radio_multiple,
    conditional_radio_other,
    conditional_value,
    display_link,
    option_toggle,
    radio,
    radio_other,
    radio_toggle,
    text,
    textarea,
    text_group,
)
from .errors import SynopticConfigurationError
from .output import (
    build_word_table,
    render_copyable_table,
)
from .rows import build_rows_from_synoptic
from .widgets import (
    field_label,
    get_field_value,
    handle_exclusive_checkbox,
)


__all__ = [
    "SynopticConfigurationError",
    "build_rows_from_synoptic",
    "build_word_table",
    "checkbox_group",
    "conditional_radio",
    "conditional_radio_multiple",
    "conditional_radio_other",
    "conditional_value",
    "display_link",
    "field_label",
    "get_field_value",
    "handle_exclusive_checkbox",
    "option_toggle",
    "radio",
    "radio_other",
    "radio_toggle",
    "render_copyable_table",
    "text",
    "textarea",
    "text_group",
]