import importlib
import pkgutil

import streamlit as st

import data

from helpers import (
    build_rows_from_synoptic,
    render_copyable_table,
)


class SynopticConfigurationError(Exception):
    """Raised when a synoptic data module is missing or contains invalid data."""


def load_synoptics() -> tuple[dict, dict]:
    """Dynamically load and validate synoptic definitions."""

    if not hasattr(data, "__path__"):
        raise SynopticConfigurationError(
            "The 'data' module must be a Python package containing "
            "an __init__.py file."
        )

    synoptics = {}
    hidden_table_values = {}

    for module_info in pkgutil.iter_modules(data.__path__):
        module_name = module_info.name

        # Ignore private and support modules.
        if module_name.startswith("_"):
            continue

        full_module_name = f"data.{module_name}"

        try:
            module = importlib.import_module(full_module_name)
        except Exception as exc:
            raise SynopticConfigurationError(
                f"Unable to import synoptic module "
                f"'{full_module_name}'."
            ) from exc

        if not hasattr(module, "DISPLAY_NAME"):
            raise SynopticConfigurationError(
                f"Module '{full_module_name}' is missing DISPLAY_NAME."
            )

        if not hasattr(module, "SYNOPTIC"):
            raise SynopticConfigurationError(
                f"Module '{full_module_name}' is missing SYNOPTIC."
            )

        display_name = module.DISPLAY_NAME
        synoptic = module.SYNOPTIC
        hidden_values = getattr(
            module,
            "HIDDEN_TABLE_VALUES",
            set(),
        )

        if not isinstance(display_name, str):
            raise TypeError(
                f"{full_module_name}.DISPLAY_NAME must be a string, "
                f"not {type(display_name).__name__}."
            )

        if not display_name.strip():
            raise ValueError(
                f"{full_module_name}.DISPLAY_NAME cannot be empty."
            )

        if not isinstance(synoptic, (list, dict)):
            raise TypeError(
                f"{full_module_name}.SYNOPTIC must be a list or "
                f"dictionary, not {type(synoptic).__name__}."
            )

        if not synoptic:
            raise ValueError(
                f"{full_module_name}.SYNOPTIC cannot be empty."
            )

        if display_name in synoptics:
            raise SynopticConfigurationError(
                f"Duplicate DISPLAY_NAME '{display_name}' found in "
                f"module '{full_module_name}'."
            )

        synoptics[display_name] = synoptic
        hidden_table_values[display_name] = hidden_values

    if not synoptics:
        raise SynopticConfigurationError(
            "No valid synoptic modules were found in the data package."
        )

    sorted_synoptics = dict(sorted(synoptics.items()))

    sorted_hidden_values = {
        display_name: hidden_table_values[display_name]
        for display_name in sorted_synoptics
    }

    return sorted_synoptics, sorted_hidden_values


st.set_page_config(
    page_title="Pathology Synoptic Generator",
    layout="centered",
)

st.title("Pathology Synoptic Generator")

synoptics, hidden_table_values = load_synoptics()

selected = st.selectbox(
    "Choose Synoptic",
    options=list(synoptics.keys()),
)

if selected not in synoptics:
    raise KeyError(
        f"The selected synoptic '{selected}' was not found."
    )

rows = build_rows_from_synoptic(
    synoptics[selected],
    hidden_table_values=hidden_table_values.get(
        selected,
        set(),
    ),
)

if rows is None:
    raise ValueError(
        f"build_rows_from_synoptic() returned None for '{selected}'."
    )

if not isinstance(rows, list):
    raise TypeError(
        "build_rows_from_synoptic() must return a list, "
        f"not {type(rows).__name__}."
    )

st.subheader("Preview")
render_copyable_table(rows)