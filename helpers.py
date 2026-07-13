"""Compatibility imports for the synoptic engine.

New code may import directly from synoptic_engine. Existing data modules
can continue importing these functions from helpers.
"""

from synoptic_engine.definitions import (
    checkbox_group,
    conditional_radio,
    conditional_radio_multiple,
    conditional_radio_other,
    conditional_value,
    option_toggle,
    radio,
    radio_other,
    radio_toggle,
    text,
    textarea,
)
from synoptic_engine.errors import SynopticConfigurationError
from synoptic_engine.output import (
    build_word_table,
    render_copyable_table,
)
from synoptic_engine.rows import build_rows_from_synoptic


from synoptic_engine.widgets import (
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
]