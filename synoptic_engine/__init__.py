"""Core package for the pathology synoptic generator."""

from .errors import SynopticConfigurationError
from .validation import (
    validate_field,
    validate_output_row,
    validate_rows,
    validate_synoptic,
)

__all__ = [
    "SynopticConfigurationError",
    "validate_field",
    "validate_output_row",
    "validate_rows",
    "validate_synoptic",
]
