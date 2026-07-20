"""HTML report generation and clipboard rendering for synoptic output."""

from __future__ import annotations

import html
from collections.abc import Sequence
from typing import Any

from .validation import validate_rows


EXCLUDED_ROW_VALUES = frozenset(
    {
        "",
        None,
        "Do not include",
        "Not applicable",
    }
)

EXCLUDED_INDENT_VALUES = frozenset(
    {
        "",
        None,
        "Do not include",
    }
)


def build_word_table(rows: Sequence[tuple[Any, ...]]) -> str:
    """Build an HTML table suitable for copying into Microsoft Word."""
    validate_rows(rows)

    table_rows: list[str] = []

    for row in rows:
        row_type = row[0]

        if row_type == "title":
            _, label, value = row

            table_rows.append(
                f"""
                <tr>
                    <td colspan="2"
                        style="
                            font-size:14pt;
                            font-weight:bold;
                            text-align:center;
                            background:#cfcfcf;
                            border:2px solid black;
                            padding:8px;
                        ">
                        {html.escape(str(label))}: {html.escape(str(value))}
                    </td>
                </tr>
                """
            )

        elif row_type == "section":
            _, label = row

            table_rows.append(
                f"""
                <tr>
                    <td colspan="2"
                        style="
                            font-weight:bold;
                            border-top:2px solid black;
                            border-left:1px solid black;
                            border-right:1px solid black;
                            border-bottom:1px solid black;
                            padding:6px;
                        ">
                        {html.escape(str(label))}
                    </td>
                </tr>
                """
            )

        elif row_type == "row":
            _, label, value = row

            if value in EXCLUDED_ROW_VALUES:
                continue

            table_rows.append(
                f"""
                <tr>
                    <td style="
                        width:35%;
                        font-weight:bold;
                        border:1px solid black;
                        padding:6px;
                        vertical-align:top;
                    ">
                        {html.escape(str(label))}:
                    </td>

                    <td style="
                        width:65%;
                        border:1px solid black;
                        padding:6px;
                        vertical-align:top;
                    ">
                        {html.escape(str(value))}
                    </td>
                </tr>
                """
            )

        elif row_type == "indent":
            _, label, value = row

            if value in EXCLUDED_INDENT_VALUES:
                continue

            table_rows.append(
                f"""
                <tr>
                    <td style="
                        width:35%;
                        font-weight:bold;
                        border:1px solid black;
                        padding:6px 6px 6px 24px;
                        vertical-align:top;
                    ">
                        - {html.escape(str(label))}:
                    </td>

                    <td style="
                        width:65%;
                        border:1px solid black;
                        padding:6px;
                        vertical-align:top;
                    ">
                        {html.escape(str(value))}
                    </td>
                </tr>
                """
            )
        
        elif row_type == "indent2":
            _, label, value = row

            if value in EXCLUDED_INDENT_VALUES:
                continue

            table_rows.append(
                f"""
                <tr>
                    <td style="
                        width:35%;
                        font-weight:bold;
                        border:1px solid black;
                        padding:6px 6px 6px 42px;
                        vertical-align:top;
                    ">
                        - {html.escape(str(label))}:
                    </td>

                    <td style="
                        width:65%;
                        border:1px solid black;
                        padding:6px;
                        vertical-align:top;
                    ">
                        {html.escape(str(value))}
                    </td>
                </tr>
                """
            )

    return f"""
    <table style="
        border-collapse:collapse;
        width:100%;
        font-family:Arial;
        font-size:11pt;
    ">
        {''.join(table_rows)}
    </table>
    """


def render_copyable_table(
    rows: Sequence[tuple[Any, ...]],
    *,
    height: int = 900,
    scrolling: bool = True,
) -> None:
    """Render the report table with a copy-to-clipboard button."""
    if not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer.")

    if not isinstance(scrolling, bool):
        raise TypeError("scrolling must be True or False.")

    try:
        import streamlit.components.v1 as components
    except ImportError as exc:
        raise RuntimeError(
            "Streamlit is required to render the copyable table. "
            "Install it with 'python -m pip install streamlit'."
        ) from exc

    html_table = build_word_table(rows)

    components.html(
        f"""
        <div id="table_to_copy">
            {html_table}
        </div>

        <br>

        <button type="button" onclick="copyTable()">
            Copy table to clipboard
        </button>

        <script>
        function copyTable() {{
            const table = document.getElementById("table_to_copy");

            if (!table) {{
                alert("The table could not be found.");
                return;
            }}

            const range = document.createRange();
            range.selectNode(table);

            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);

            const copied = document.execCommand("copy");
            selection.removeAllRanges();

            if (copied) {{
                alert("Table copied!");
            }} else {{
                alert("The table could not be copied.");
            }}
        }}
        </script>
        """,
        height=height,
        scrolling=scrolling,
    )


__all__ = [
    "build_word_table",
    "render_copyable_table",
]
