"""Breast DCIS resection, transcribed from the supplied AJCC 8 case summary.

Plus-marked fields in the supplied outline are optional. The repeated Other /
Cannot be determined lines in its nodal section belong to the ENE and nodal
tumor-status choices, following the existing breast resection layout.
"""

from synoptic_engine import (
    checkbox_group,
    conditional_radio_multiple,
    conditional_value,
    option_toggle,
    radio,
    radio_toggle,
    text,
)

DISPLAY_NAME = "Breast DCIS, Resection"
HIDDEN_TABLE_VALUES = set()
TNM_DEFINITIONS_KEY = "show_breast_dcis_tnm_definitions"

MARGINS_WITHIN_2_MM = "DCIS present within 0-2 mm of final margins"
NODES_PRESENT = "Regional lymph nodes present"
NODES_POSITIVE = "Tumor present in regional lymph node(s)"


def specified_value(label, options, key, *, optional=False, values=None):
    """Use the existing choice-and-text widget for specified findings."""
    value_fields = {}
    if "Other" in options:
        value_fields["Other"] = (f"Specify Other {label}", "")
    if "Cannot be determined" in options:
        value_fields["Cannot be determined"] = ("Explain", "")
    value_fields.update(values or {})
    return conditional_value(
        label=label,
        options=(["Do not include"] if optional else []) + options,
        value_fields=value_fields,
        key=f"breast_dcis_{key}",
    )


def node_number(label, key, *, optional=False, not_applicable=False):
    return specified_value(
        label,
        (["Not applicable"] if not_applicable else [])
        + ["Exact number", "Other", "Cannot be determined"],
        key,
        optional=optional,
        values={"Exact number": ("Specify Exact Number", "")},
    )


def node_measurement(label, key, *, optional=False, exact="Exact size"):
    return specified_value(
        label,
        [exact, "Other", "Cannot be determined"],
        key,
        optional=optional,
        values={exact: ("Specify Measurement in Millimeters (mm)", " mm")},
    )


def margin_details():
    fields = [
        specified_value(
            label,
            ["None identified", "Specify"],
            key,
            values={"Specify": ("Specify Margin(s)", "")},
        )
        for label, key in [
            ("Margin(s) Involved by DCIS (at ink)", "margins_at_ink"),
            (
                "Margin(s) Less than 1 mm from DCIS (but not at ink)",
                "margins_less_than_1_mm",
            ),
            ("Margin(s) 1 to 2 mm from DCIS", "margins_1_to_2_mm"),
        ]
    ]
    fields.append(
        specified_value(
            "Margin(s) Greater than 2 mm from DCIS",
            ["All Remaining Margins", "None identified", "Specify"],
            "margins_greater_than_2_mm",
            optional=True,
            values={"Specify": ("Specify Margin(s)", "")},
        )
    )
    return fields


PN_CATEGORY_OPTIONS = [
    (
        "pN not assigned (no nodes submitted or found)",
        "pN not assigned (no nodes submitted or found)",
    ),
    (
        "pN not assigned (cannot be determined based on available pathological information)",
        "pN not assigned",
    ),
    ("pN0: No regional lymph node metastasis identified or ITCs only", "pN0"),
    (
        "pN0 (i+): ITCs only (malignant cell clusters no larger than 0.2 mm) "
        "in regional lymph node(s)",
        "pN0 (i+)",
    ),
    (
        "pN0 (mol+): Positive molecular findings by reverse transcriptase "
        "polymerase chain reaction (RT-PCR); no ITCs detected",
        "pN0 (mol+)",
    ),
    (
        "pN1mi: Micrometastases (approximately 200 cells, larger than 0.2 mm, "
        "but none larger than 2.0 mm)",
        "pN1mi",
    ),
    (
        "pN1a: Metastases in 1-3 axillary lymph nodes, at least one metastasis "
        "larger than 2.0 mm",
        "pN1a",
    ),
    (
        "pN1b: Metastases in ipsilateral internal mammary sentinel nodes, excluding ITCs",
        "pN1b",
    ),
    ("pN1c: pN1a and pN1b combined", "pN1c"),
    (
        "pN2a: Metastases in 4-9 axillary lymph nodes, at least one tumor deposit "
        "larger than 2.0 mm",
        "pN2a",
    ),
    (
        "pN2b: Metastases in clinically detected internal mammary lymph nodes "
        "with or without microscopic confirmation; with pathologically negative axillary nodes",
        "pN2b",
    ),
    (
        "pN3a: Metastases in 10 or more axillary lymph nodes (at least one tumor deposit "
        "larger than 2.0 mm); or metastases to the infraclavicular (Level III axillary lymph) nodes",
        "pN3a",
    ),
    (
        "pN3b: pN1a or pN2a in the presence of cN2b (positive internal mammary nodes "
        "by imaging); or pN2a in the presence of pN1b",
        "pN3b",
    ),
    ("pN3c: Metastases in ipsilateral supraclavicular lymph nodes", "pN3c"),
]


SYNOPTIC = [
    ("title", "CASE SUMMARY", "(DCIS OF THE BREAST: Resection) Standard(s): AJCC 8"),
    ("section", "SPECIMEN"),
    specified_value(
        "Procedure",
        [
            "Excision (less than total mastectomy, including lumpectomy and partial mastectomy)",
            "Total mastectomy (including nipple-sparing and skin-sparing mastectomy)",
            "Other",
            "Not specified",
        ],
        "procedure",
    ),
    radio(
        "Specimen Laterality", ["Right", "Left", "Not specified"],
        key="breast_dcis_laterality",
    ),
    ("section", "TUMOR"),
    checkbox_group(
        label="Tumor Site",
        options=[
            "Do not include", "Upper outer quadrant", "Upper inner quadrant",
            "Lower outer quadrant", "Lower inner quadrant", "Central", "Retroareolar",
            *[f"{hour} o'clock" for hour in range(1, 13)], "Not specified",
        ],
        default="Do not include",
        exclusive_options=["Do not include", "Not specified"],
        key="breast_dcis_tumor_site",
    ),
    specified_value(
        "Histologic Type",
        [
            "Ductal carcinoma in situ (DCIS)", "Paget disease",
            "Encapsulated papillary carcinoma in situ", "Solid papillary carcinoma in situ",
            "Other histologic type not listed",
        ],
        "histologic_type",
        values={"Other histologic type not listed": ("Specify Other Histologic Type", "")},
    ),
    specified_value(
        "Size (Extent) of DCIS",
        ["At least (estimated size in Millimeters)", "Cannot be determined"],
        "size",
        values={"At least (estimated size in Millimeters)": ("Specify Estimated Size (Extent)", " mm")},
    ),
    text("Size of DCIS Comment", key="breast_dcis_size_comment"),
    checkbox_group(
        label="Architectural Pattern(s)",
        options=[
            "Do not include", "Comedo", "Cribriform", "Micropapillary", "Papillary",
            "Solid", "Solid papillary carcinoma in situ", "Encapsulated papillary carcinoma in situ",
            "Paget disease (DCIS involving nipple skin)", "Other",
        ],
        conditional_fields={"Other": text("Other Architectural Pattern", key="breast_dcis_pattern_other")},
        default="Do not include",
        exclusive_options=["Do not include"],
        key="breast_dcis_patterns",
    ),
    specified_value(
        "Nuclear Grade",
        ["Grade I (low)", "Grade II (intermediate)", "Grade III (high)", "Other", "Cannot be determined"],
        "grade",
    ),
    text("Nuclear Grade Comment", key="breast_dcis_grade_comment"),
    specified_value(
        "Necrosis",
        [
            "Not identified", "Present, focal (small foci or single cell necrosis)",
            'Present, central (expansive "comedo" necrosis)', "Other", "Cannot be determined",
        ],
        "necrosis",
    ),
    checkbox_group(
        label="Additional Lesion(s)",
        options=[
            "Do not include", "Not identified", "Lobular carcinoma in situ, classic",
            "Lobular carcinoma in situ, pleomorphic", "Lobular carcinoma in situ (specify)",
            "Atypical lobular hyperplasia", "Atypical ductal hyperplasia", "Flat epithelial atypia", "Other",
        ],
        conditional_fields={
            "Lobular carcinoma in situ (specify)": text("LCIS Type", key="breast_dcis_lcis_type"),
            "Other": text("Other Additional Lesion", key="breast_dcis_lesion_other"),
        },
        default="Do not include",
        exclusive_options=["Do not include", "Not identified"],
        key="breast_dcis_additional_lesions",
    ),
    text("Extent of LCIS", key="breast_dcis_lcis_extent"),
    text("Additional Lesion(s) Comment", key="breast_dcis_lesion_comment"),
    checkbox_group(
        label="Microcalcifications",
        options=["Do not include", "Not identified", "Present in DCIS", "Present in non-neoplastic tissue", "Other"],
        conditional_fields={"Other": text("Other Microcalcifications", key="breast_dcis_calcifications_other")},
        default="Do not include",
        exclusive_options=["Do not include", "Not identified"],
        key="breast_dcis_calcifications",
    ),
    ("section", "MARGINS"),
    conditional_radio_multiple(
        label="Final Margin Status for DCIS",
        options=[
            "Not applicable (no residual DCIS in specimen)",
            "All final margins greater than 2 mm from DCIS", MARGINS_WITHIN_2_MM,
            "Other", "Cannot be determined",
        ],
        conditional_fields={
            MARGINS_WITHIN_2_MM: margin_details(),
            "Cannot be determined": text("Explain Margin Status", key="breast_dcis_margin_explanation"),
        },
        key="breast_dcis_margin_status",
    ),
    
    ("section", "REGIONAL LYMPH NODES"),
    conditional_radio_multiple(
        label="Regional Lymph Node Status",
        options=["Not applicable (no regional lymph nodes submitted or found)", NODES_PRESENT],
        conditional_fields={
            NODES_PRESENT: [
                conditional_radio_multiple(
                    label="Regional Lymph Node Tumor Status",
                    options=["All regional lymph nodes negative for tumor", NODES_POSITIVE, "Other", "Cannot be determined"],
                    conditional_fields={
                        NODES_POSITIVE: [
                            node_number("Number of Lymph Nodes with Macrometastases (greater than 2 mm)", "nodes_macro"),
                            node_number(
                                "Number of Lymph Nodes with Micrometastases (greater than 0.2 mm to 2 mm and / or greater than 200 cells)",
                                "nodes_micro",
                            ),
                            node_number(
                                "Number of Lymph Nodes with Isolated Tumor Cells (0.2 mm or less OR 200 cells or less)",
                                "nodes_itc", not_applicable=True,
                            ),
                            node_number(
                                "Total Number of Positive Macroscopic and Microscopic Lymph Nodes Counted Towards pN Category",
                                "nodes_positive_total", optional=True,
                            ),
                            node_measurement("Size of Largest Nodal Metastatic Deposit", "nodal_deposit_size"),
                            conditional_radio_multiple(
                                label="Extranodal Extension (ENE)",
                                options=["Not identified", "Present", "Other", "Cannot be determined"],
                                conditional_fields={
                                    "Present": [
                                        node_measurement(
                                            "Largest Measurement of Extranodal Extension", "ene_size",
                                            optional=True, exact="Exact measurement",
                                        ),
                                        node_number("Number of Lymph Nodes with Extranodal Extension", "ene_nodes", optional=True),
                                    ],
                                    "Cannot be determined": text("Explain Extranodal Extension", key="breast_dcis_ene_explanation"),
                                },
                                key="breast_dcis_ene",
                            ),
                        ],
                        "Cannot be determined": text("Explain Regional Lymph Node Tumor Status", key="breast_dcis_node_status_explanation"),
                    },
                    key="breast_dcis_node_tumor_status",
                ),
                node_number("Total Number of Lymph Nodes Examined (sentinel and non-sentinel)", "nodes_examined"),
            ],
        },
        key="breast_dcis_node_status",
    ),
    ("section", "DISTANT METASTASIS"),
    checkbox_group(
        label="Distant Site(s) Involved, if applicable",
        options=["Not applicable", "Non-regional lymph node(s)", "Lung", "Liver", "Bone", "Brain", "Other", "Cannot be determined"],
        conditional_fields={
            site: text(
                "Explain Distant Site(s)" if site == "Cannot be determined" else f"{site} Details",
                key=f"breast_dcis_distant_{index}",
            )
            for index, site in enumerate(["Non-regional lymph node(s)", "Lung", "Liver", "Bone", "Brain", "Other", "Cannot be determined"])
        },
        default="Not applicable",
        exclusive_options=["Not applicable", "Cannot be determined"],
        key="breast_dcis_distant_sites",
    ),
    ("section", "pTNM CLASSIFICATION (AJCC 8th Edition)"),
    option_toggle("Show pTNM definitions in table", key=TNM_DEFINITIONS_KEY),
    checkbox_group(
        label="Modified Classification",
        options=["Not applicable", "y (post-neoadjuvant therapy)", "r (recurrence)"],
        default="Not applicable",
        exclusive_options=["Not applicable"],
        key="breast_dcis_modified_classification",
    ),
    radio_toggle(
        label="pT Category",
        options=[
            ("pTis (DCIS): Ductal carcinoma in situ", "pTis (DCIS)"),
            (
                "pTis (Paget): Paget disease of the nipple NOT associated with invasive carcinoma "
                "and / or DCIS in the underlying breast parenchyma",
                "pTis (Paget)",
            ),
        ],
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_dcis_pt",
    ),
    radio_toggle(
        label="T Suffix",
        options=[("Not applicable", "Not applicable"), ("(m) multiple primary synchronous tumors in a single organ", "(m)")],
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_dcis_t_suffix",
    ),
    radio_toggle("pN Category", PN_CATEGORY_OPTIONS, TNM_DEFINITIONS_KEY, key="breast_dcis_pn"),
    radio_toggle(
        label="N Suffix",
        options=[
            ("Not applicable", "Not applicable"),
            (
                "(sn): Sentinel node(s) evaluated. If 6 or more nodes (sentinel or nonsentinel) "
                "are removed, this modifier should not be used.",
                "(sn)",
            ),
            ("(f): Nodal metastasis confirmed by fine needle aspiration or core needle biopsy.", "(f)"),
        ],
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_dcis_n_suffix",
    ),
    radio(
        label="pM Category",
        options=[
            "Do not include",
            "Not applicable - pM cannot be determined from the submitted specimen(s)",
            "pM1: Histologically proven metastases larger than 0.2 mm",
        ],
        key="breast_dcis_pm",
    ),
]
