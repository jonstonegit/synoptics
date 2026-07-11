import html

import streamlit as st
import streamlit.components.v1 as components


def build_word_table(rows: list[tuple]) -> str:
    table_rows = ""

    for row in rows:
        row_type = row[0]

        if row_type == "title":
            _, label, value = row

            table_rows += f"""
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
                    {html.escape(label)}: {html.escape(value)}
                </td>
            </tr>
            """

        elif row_type == "section":
            _, label = row

            table_rows += f"""
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
                    {html.escape(label)}
                </td>
            </tr>
            """

        elif row_type == "row":
            _, label, value = row

            if value in ("", None, "Do not include", "Not applicable"):
                continue

            table_rows += f"""
            <tr>
                <td style="
                    width:35%;
                    font-weight:bold;
                    border:1px solid black;
                    padding:6px;
                    vertical-align:top;
                ">
                    {html.escape(label)}:
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
        elif row_type == "indent":
            _, label, value = row

            if value in ("", None, "Do not include"):
                continue

            table_rows += f"""
            <tr>
                <td style="
                    width:35%;
                    font-weight:bold;
                    border:1px solid black;
                    padding:6px 6px 6px 24px;
                    vertical-align:top;
                ">
                    - {html.escape(label)}:
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

    return f"""
    <table style="
        border-collapse:collapse;
        width:100%;
        font-family:Arial;
        font-size:11pt;
    ">
        {table_rows}
    </table>
    """

def field_label(label: str) -> None:
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
    field: dict,
    indent_level: int = 0,
):
    if indent_level == 0:
        return _get_field_value(field, indent_level)

    indent_width = min(indent_level * 0.03, 0.15)

    _, content_column = st.columns(
        [indent_width, 1 - indent_width]
    )

    with content_column:
        return _get_field_value(field, indent_level)

def _get_field_value(
    field: dict,
    indent_level: int,
):
    label = field["label"]
    field_type = field["type"]

    if field_type == "radio":

        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        return label, value, []

    if field_type == "radio_other":

        field_label(label)

        value = st.radio(
            "",
            field["options"] + ["Other"],
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{field.get('key', label)}_other",
            )

        return label, value, []

    if field_type == "conditional_radio":
        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        child_rows = []

        if value == field["trigger"]:
            subvalue = st.selectbox(
                field["sublabel"],
                field["suboptions"],
                key=f"{field.get('key', label)}_{field['sublabel']}",
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
            field["options"] + ["Other"],
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        child_rows = []

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{field.get('key', label)}_other",
            )
            return label, value, child_rows

        if value == field["trigger"]:
            subvalue = st.selectbox(
                field["sublabel"],
                field["suboptions"],
                key=f"{field.get('key', label)}_{field['sublabel']}",
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

        key = field.get("key", label)

        value = st.text_input(
            f"Specify {label}",
            key=f"{field.get('key', label)}_other",
        )

        suffix = field.get("suffix", "")

        if value != "":
            value += suffix

        return label, value, []

    if field_type == "textarea":

        value = st.text_area(
            label,
            key=field.get("key", label),
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
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        if value == "Other":
            value = st.text_input(
                f"Specify {label}",
                key=f"{field.get('key', label)}_other",
            )

            return label, value, []

        child_rows = []

        if value in field["conditional_fields"]:
            configured_children = field["conditional_fields"][value]

            # Allow either one child dictionary or a list of children.
            if isinstance(configured_children, dict):
                configured_children = [configured_children]

            for child_field in configured_children:
                child_label, child_value, child_children = get_field_value(
                    child_field,
                    indent_level + 1,
                )

                child_rows.append(
                    ("indent", child_label, child_value)
                )
                child_rows.extend(child_children)

        return label, value, child_rows
    
    if field_type == "checkbox_group":
        selected_values = []
        child_rows = []

        field_label(label)

        base_key = field.get("key", label)
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

            if is_checked:
                selected_values.append(option)

                if option in field["conditional_fields"]:
                    configured_children = field["conditional_fields"][option]

                    # Accept either one field dictionary or a list of field dictionaries.
                    if isinstance(configured_children, dict):
                        configured_children = [configured_children]

                    for child_field in configured_children:
                        child_label, child_value, child_children = get_field_value(
                            child_field,
                            indent_level + 1,
                        )

                        child_rows.append(
                            ("indent", child_label, child_value)
                        )
                        child_rows.extend(child_children)

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
            key=field.get("key", f"{label}_radio"),
            label_visibility="collapsed",
        )

        selected_short = next(
            short_text
            for full_text, short_text in field["options"]
            if full_text == selected_display
        )

        show_full = st.session_state.get(
            field["session_key"],
            False,
        )

        value = selected_display if show_full else selected_short

        return label, value, []

    if field_type == "option_toggle":
        st.markdown(
            "<span style='font-size:18px; font-weight:bold;'>Table Options</span>",
            unsafe_allow_html=True,
        )
        st.checkbox(
            label,
            value=field.get("default", False),
            key=field["key"],
        )
        
        return label, "", []

    if field_type == "conditional_value":

        field_label(label)

        value = st.radio(
            "",
            field["options"],
            key=field.get("key", label),
            label_visibility="collapsed",
        )

        if value == "Not applicable":
            return label, "", []

        if value in field["value_fields"]:
            prompt, suffix = field["value_fields"][value]

            entered = st.text_input(
                prompt,
                key=f"{label}_{value}",
            )

            if entered:
                if suffix:
                    entered += suffix

                if value == "Exact size":
                    return label, entered, []

                if value == "Exact number":
                    return label, entered, []

                if value == "Exact distance in cm":
                    return label, entered, []

                if value == "Exact distance in mm":
                    return label, entered, []

                if value == "At least":
                    return label, f"At least {entered}", []

                if value == "Other":
                    return label, value, [("indent", "Comment", entered)]

                if value == "Cannot be determined":
                    return label, value, [("indent", "Comment", entered)]

        return label, value, []

    raise ValueError(
        f"Unsupported field type {field_type!r} "
        f"for field {label!r}. Full field: {field!r}"
    )


def build_rows_from_synoptic(synoptic):

    rows = []

    for item in synoptic:

        if isinstance(item, tuple):

            rows.append(item)

        else:

            label, value, child_rows = get_field_value(item)

            rows.append(("row", label, value))

            for child_row in child_rows:
                rows.append(child_row)

    return rows


def render_copyable_table(rows):

    html_table = build_word_table(rows)

    components.html(
        f"""
        <div id="table_to_copy">
            {html_table}
        </div>

        <br>

        <button onclick="copyTable()">
            Copy table to clipboard
        </button>

        <script>
        function copyTable() {{
            const table = document.getElementById("table_to_copy");
            const range = document.createRange();
            range.selectNode(table);

            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);

            document.execCommand("copy");

            window.getSelection().removeAllRanges();

            alert("Table copied!");
        }}
        </script>
        """,
        height=900,
        scrolling=True,
    )

def radio(
    label: str,
    options: list[str],
    key: str | None = None,
) -> dict:
    return {
        "type": "radio",
        "label": label,
        "options": options,
        "key": key or label,
    }


def radio_other(label: str, options: list[str]) -> dict:
    return {
        "type": "radio_other",
        "label": label,
        "options": options,
    }


def text(label: str, suffix: str = "", key: str | None = None) -> dict:
    return {
        "type": "text",
        "label": label,
        "suffix": suffix,
        "key": key or label,
    }


def textarea(label: str) -> dict:
    return {
        "type": "textarea",
        "label": label,
    }


def conditional_radio(
    label: str,
    options: list[str],
    trigger: str,
    sublabel: str,
    suboptions: list[str],
) -> dict:
    return {
        "type": "conditional_radio",
        "label": label,
        "options": options,
        "trigger": trigger,
        "sublabel": sublabel,
        "suboptions": suboptions,
    }


def conditional_radio_other(
    label: str,
    options: list[str],
    trigger: str,
    sublabel: str,
    suboptions: list[str],
) -> dict:
    return {
        "type": "conditional_radio_other",
        "label": label,
        "options": options,
        "trigger": trigger,
        "sublabel": sublabel,
        "suboptions": suboptions,
    }

def conditional_radio_multiple(
    label: str,
    options: list[str],
    conditional_fields: dict[str, list[dict]],
    allow_other: bool = False,
) -> dict:
    return {
        "type": "conditional_radio_multiple",
        "label": label,
        "options": options,
        "conditional_fields": conditional_fields,
        "allow_other": allow_other,
    }

def checkbox_group(
    label: str,
    options: list[str],
    conditional_fields: dict[str, dict | list[dict]] | None = None,
    comment: bool = False,
    default: str | None = None,
    exclusive_options: list[str] | None = None,
    key: str | None = None,
) -> dict:
    return {
        "type": "checkbox_group",
        "label": label,
        "options": options,
        "conditional_fields": conditional_fields or {},
        "comment": comment,
        "default": default,
        "exclusive_options": exclusive_options or [],
        "key": key or label,
    }

def conditional_value(
    label: str,
    options: list[str],
    value_fields: dict[str, tuple[str, str]],
) -> dict:
    return {
        "type": "conditional_value",
        "label": label,
        "options": options,
        "value_fields": value_fields,
    }

def radio_toggle(
    label: str,
    options: list[tuple[str, str]],
    session_key: str,
    key: str | None = None,
) -> dict:
    return {
        "type": "radio_toggle",
        "label": label,
        "options": options,
        "session_key": session_key,
        "key": key or f"{label}_radio",
    }

def option_toggle(
    label: str,
    key: str,
    default: bool = False,
) -> dict:
    return {
        "type": "option_toggle",
        "label": label,
        "key": key,
        "default": default,
    }

def handle_exclusive_checkbox(
    changed_key: str,
    option_keys: dict[str, str],
    exclusive_options: list[str],
) -> None:
    if not st.session_state.get(changed_key, False):
        return

    changed_option = next(
        option
        for option, key in option_keys.items()
        if key == changed_key
    )

    if changed_option in exclusive_options:
        # An exclusive option was selected:
        # uncheck every other option.
        for option, key in option_keys.items():
            if option != changed_option:
                st.session_state[key] = False
    else:
        # A regular option was selected:
        # uncheck all exclusive options.
        for exclusive_option in exclusive_options:
            exclusive_key = option_keys.get(exclusive_option)

            if exclusive_key is not None:
                st.session_state[exclusive_key] = False