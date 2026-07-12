"""Convert validated synoptic definitions into report-output rows."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .errors import SynopticConfigurationError
from .validation import (
    validate_output_row,
    validate_synoptic,
)


OutputRow = tuple[Any, ...]
FieldResult = tuple[str, Any, list[OutputRow]]
FieldRenderer = Callable[[dict[str, Any]], FieldResult]


def _load_default_field_renderer() -> FieldRenderer:
    """Load the Streamlit field renderer only when it is needed."""
    try:
        from .widgets import get_field_value
    except ImportError as exc:
        raise SynopticConfigurationError(
            "The default field renderer could not be imported from "
            "'synoptic_engine.widgets'. Create widgets.py or pass a "
            "field_renderer argument to build_rows_from_synoptic()."
        ) from exc

    return get_field_value


def _validate_field_result(
    result: Any,
    *,
    item_index: int,
) -> FieldResult:
    """Validate the result returned by a field-rendering function."""
    context = f"field renderer result for synoptic item {item_index}"

    if not isinstance(result, tuple) or len(result) != 3:
        raise SynopticConfigurationError(
            f"{context} must be a three-item tuple: "
            "(label, value, child_rows)."
        )

    label, value, child_rows = result

    if not isinstance(label, str) or not label.strip():
        raise SynopticConfigurationError(
            f"{context}: label must be a non-empty string."
        )

    if not isinstance(child_rows, list):
        raise SynopticConfigurationError(
            f"{context}: child_rows must be a list, not "
            f"{type(child_rows).__name__}."
        )

    for child_index, child_row in enumerate(child_rows):
        validate_output_row(child_row, child_index)

    return label, value, child_rows


def build_rows_from_synoptic(
    synoptic: Any,
    *,
    field_renderer: FieldRenderer | None = None,
    hidden_table_values: set[str] | list[str] | None = None,
) -> list[OutputRow]:
    """Render all fields and convert a synoptic into output rows."""

    validate_synoptic(synoptic)

    renderer = field_renderer or _load_default_field_renderer()
    hidden_values = set(hidden_table_values or [])

    rows: list[OutputRow] = []

    for item_index, item in enumerate(synoptic):
        if isinstance(item, tuple):
            validate_output_row(item, item_index)
            rows.append(item)
            continue

        result = renderer(item)

        label, value, child_rows = _validate_field_result(
            result,
            item_index=item_index,
        )

        # Keep the table row, but hide matching words in its value column.
        if isinstance(value, str) and value in hidden_values:
            value = "\u00A0"

        parent_row: OutputRow = ("row", label, value)

        validate_output_row(parent_row, item_index)
        rows.append(parent_row)
        rows.extend(child_rows)

    return rows


__all__ = [
    "FieldRenderer",
    "OutputRow",
    "build_rows_from_synoptic",
]
