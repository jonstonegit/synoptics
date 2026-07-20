from synoptic_engine import (
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

DISPLAY_NAME = "Breast Invasive, Resection"

HIDDEN_TABLE_VALUES = {
    "Do not include additional findings section",
    "Do not include special studies section",
}

SIMILAR_TUMOR_FOCI = (
                "Multiple foci of invasive carcinoma with similar features "
                "(e.g., satellites or post-treatment foci of the same "
                "histologic type, grade, and biomarkers)"
            )

DIFFERENT_TUMOR_FOCI = "Multiple foci of invasive carcinoma with different features"

MARGIN_LOCATIONS = [
    "Anterior",
    "Posterior",
    "Superior",
    "Inferior",
    "Lateral",
    "Medial",
]

TNM_DEFINITIONS_KEY = "show_breast_tnm_definitions"


MODIFIED_CLASSIFICATION_OPTIONS = [
    (
        "Not applicable",
        "Not applicable",
    ),
    (
        "y (post-neoadjuvant therapy)",
        "y",
    ),
    (
        "r (recurrence)",
        "r",
    ),
]


PT_CATEGORY_OPTIONS = [
    (
        (
            "pT not assigned "
            "(cannot be determined based on available "
            "pathological information)"
        ),
        "pT not assigned",
    ),
    (
        "pT0: No evidence of primary tumor",
        "pT0",
    ),
    (
        "pTis (DCIS): Ductal carcinoma in situ",
        "pTis (DCIS)",
    ),
    (
        (
            "pTis (Paget): Paget disease of the nipple "
            "not associated with invasive carcinoma and / or "
            "ductal carcinoma in situ in the underlying "
            "breast parenchyma"
        ),
        "pTis (Paget)",
    ),
    (
        (
            "pT1mi: Tumor less than or equal to 1 mm "
            "in greatest dimension"
        ),
        "pT1mi",
    ),
    (
        (
            "pT1a: Tumor greater than 1 mm but less than "
            "or equal to 5 mm in greatest dimension"
        ),
        "pT1a",
    ),
    (
        (
            "pT1b: Tumor greater than 5 mm but less than "
            "or equal to 10 mm in greatest dimension"
        ),
        "pT1b",
    ),
    (
        (
            "pT1c: Tumor greater than 10 mm but less than "
            "or equal to 20 mm in greatest dimension"
        ),
        "pT1c",
    ),
    (
        "pT1 (subcategory cannot be determined)",
        "pT1",
    ),
    (
        (
            "pT2: Tumor greater than 20 mm but less than "
            "or equal to 50 mm in greatest dimension"
        ),
        "pT2",
    ),
    (
        (
            "pT3: Tumor greater than 50 mm "
            "in greatest dimension"
        ),
        "pT3",
    ),
    (
        (
            "pT4a: Extension to the chest wall; invasion or "
            "adherence to pectoralis muscle in the absence of "
            "invasion of chest wall structures does not "
            "qualify as T4"
        ),
        "pT4a",
    ),
    (
        (
            "pT4b: Ulceration and / or ipsilateral satellite "
            "nodules and / or edema, including peau d'orange, "
            "of the skin which do not meet the criteria for "
            "inflammatory carcinoma"
        ),
        "pT4b",
    ),
    (
        "pT4c: Both T4a and T4b are present",
        "pT4c",
    ),
    (
        "pT4d: Inflammatory carcinoma",
        "pT4d",
    ),
    (
        "pT4 (subcategory cannot be determined)",
        "pT4",
    ),
]


T_SUFFIX_OPTIONS = [
    (
        "Not applicable",
        "Not applicable",
    ),
    (
        (
            "(m) multiple primary synchronous tumors "
            "in a single organ"
        ),
        "(m)",
    ),
]


PN_CATEGORY_OPTIONS = [
    (
        "pN not assigned (no nodes submitted or found)",
        "pN not assigned (no nodes submitted or found)",
    ),
    (
        (
            "pN not assigned "
            "(cannot be determined based on available "
            "pathological information)"
        ),
        "pN not assigned",
    ),
    (
        (
            "pN0: No regional lymph node metastasis "
            "identified or isolated tumor cells only"
        ),
        "pN0",
    ),
    (
        (
            "pN0 (i+): Isolated tumor cells only "
            "(malignant cell clusters no larger than 0.2 mm) "
            "in regional lymph node(s)"
        ),
        "pN0 (i+)",
    ),
    (
        (
            "pN0 (mol+): Positive molecular findings by "
            "reverse transcriptase polymerase chain reaction; "
            "no isolated tumor cells detected"
        ),
        "pN0 (mol+)",
    ),
    (
        (
            "pN1mi: Micrometastases, approximately 200 cells, "
            "larger than 0.2 mm, but none larger than 2.0 mm"
        ),
        "pN1mi",
    ),
    (
        (
            "pN1a: Metastases in 1-3 axillary lymph nodes, "
            "with at least one metastasis larger than 2.0 mm"
        ),
        "pN1a",
    ),
    (
        (
            "pN1b: Metastases in ipsilateral internal mammary "
            "sentinel nodes, excluding isolated tumor cells"
        ),
        "pN1b",
    ),
    (
        "pN1c: pN1a and pN1b combined",
        "pN1c",
    ),
    (
        (
            "pN2a: Metastases in 4-9 axillary lymph nodes, "
            "with at least one tumor deposit larger than 2.0 mm"
        ),
        "pN2a",
    ),
    (
        (
            "pN2b: Metastases in clinically detected internal "
            "mammary lymph nodes with or without microscopic "
            "confirmation, with pathologically negative "
            "axillary nodes"
        ),
        "pN2b",
    ),
    (
        (
            "pN3a: Metastases in 10 or more axillary lymph "
            "nodes, with at least one tumor deposit larger "
            "than 2.0 mm; or metastases to the infraclavicular "
            "(level III axillary) lymph nodes"
        ),
        "pN3a",
    ),
    (
        (
            "pN3b: pN1a or pN2a in the presence of cN2b "
            "(positive internal mammary nodes by imaging); "
            "or pN2a in the presence of pN1b"
        ),
        "pN3b",
    ),
    (
        (
            "pN3c: Metastases in ipsilateral "
            "supraclavicular lymph nodes"
        ),
        "pN3c",
    ),
]


N_SUFFIX_OPTIONS = [
    (
        "Not applicable",
        "Not applicable",
    ),
    (
        (
            "(sn): Sentinel node(s) evaluated."
        ),
        "(sn)",
    ),
    (
        (
            "(f): Nodal metastasis confirmed by fine needle "
            "aspiration or core needle biopsy"
        ),
        "(f)",
    ),
]

invasive_margin_within_2_mm = (
    "Invasive carcinoma present within 0-2 mm "
    "of final margins"
)

dcis_margin_within_2_mm = (
    "DCIS present within 0-2 mm of final margins"
)

def margin_location_field(
    label: str,
    key: str,
    *,
    specify_option: str = "Specify",
) -> dict:
    return conditional_radio_multiple(
        label=label,
        options=[
            "None identified",
            specify_option,
        ],
        conditional_fields={
            specify_option: checkbox_group(
                label="Specify Margin(s)",
                options=MARGIN_LOCATIONS,
                key=f"{key}_locations",
            ),
        },
        child_value_options=[
            specify_option,
        ],
        key=key,
    )

def invasive_margin_fields() -> list[dict]:
    return [
        margin_location_field(
            label=(
                "Margin(s) Involved by "
                "Invasive Carcinoma (at ink)"
            ),
            specify_option="Specify involved margins",
            key="invasive_margin_involved",
        ),

        margin_location_field(
            label=(
                "Margin(s) Less than 1 mm from "
                "Invasive Carcinoma (but not at ink)"
            ),
            include_do_not_include=True,
            key="invasive_margin_less_than_1_mm",
        ),

        margin_location_field(
            label=(
                "Margin(s) 1 to 2 mm from "
                "Invasive Carcinoma"
            ),
            include_do_not_include=True,
            key="invasive_margin_1_to_2_mm",
        ),

        margin_location_field(
            label=(
                "Margin(s) Greater than 2 mm from "
                "Invasive Carcinoma"
            ),
            include_do_not_include=True,
            include_other=True,
            include_cannot_be_determined=True,
            key="invasive_margin_greater_than_2_mm",
        ),
    ]


def dcis_margin_fields() -> list[dict]:
    return [
        margin_location_field(
            label="Margin(s) Involved by DCIS (at ink)",
            key="dcis_margin_involved",
        ),

        margin_location_field(
            label=(
                "Margin(s) Less than 1 mm from "
                "DCIS (but not at ink)"
            ),
            key="dcis_margin_less_than_1_mm",
        ),

        margin_location_field(
            label="Margin(s) 1 to 2 mm from DCIS",
            key="dcis_margin_1_to_2_mm",
        ),

        margin_location_field(
            label="Margin(s) Greater than 2 mm from DCIS",
            include_do_not_include=True,
            include_other=True,
            include_cannot_be_determined=True,
            key="dcis_margin_greater_than_2_mm",
        ),
    ]


def number_of_foci(key_prefix: str):
    return conditional_value(
        label="Number of Foci",
        options=[
            "Do not include",
            "Specify number",
            "At least",
            "Cannot be determined",
        ],
        value_fields={
            "Specify number": (
                "Specify Number of Foci",
                "",
            ),
            "At least": (
                "Specify Minimum Number of Foci",
                "",
            ),
            "Cannot be determined": (
                "Explain",
                "",
            ),
        },
        key=f"{key_prefix}_number_of_foci",
    )


def repeated_tumor_characteristics(
    number_of_tumors: int,
) -> list[dict]:
    fields = []

    for tumor_number in range(
        1,
        number_of_tumors + 1,
    ):
        fields.extend(
            tumor_characteristics(
                tumor_number,
                numbered=True,
            )
        )

    return fields

def tumor_characteristics(
    tumor_number: int,
    *,
    numbered: bool = False,
    include_additional_foci: bool = False,
) -> list[dict]:
    """Create one Breast Tumor Characteristics section."""

    prefix = f"tumor_{tumor_number}"

    nst_pattern = (
        "Invasive carcinoma of no special type (ductal) "
        "with specific morphologic pattern"
    )

    lobular_variant = (
        "Invasive lobular carcinoma, variant pattern"
    )

    mixed_histologic_types = (
        "Mixed histologic types"
    )

    metaplastic_mixed = (
        "Metaplastic carcinoma, mixed"
    )

    metaplastic_other = (
        "Metaplastic carcinoma, other type"
    )

    other_histologic_type = (
        "Other histologic type not listed"
    )

    exact_tumor_size = (
        "Largest contiguous focus of invasive carcinoma "
        "(specify exact measurement in Millimeters (mm))"
    )

    tumor_size_cannot_be_determined = (
        "Size of largest invasive focus cannot be determined"
    )

    characteristic_fields = [
        conditional_radio_multiple(
            label="Tumor Site",
            options=[
                "Specify tumor site / location",
                "Not specified",
            ],
            conditional_fields={
                "Specify tumor site / location": radio(
                    label="Specific Tumor Location",
                    options=[
                        "Upper outer quadrant",
                        "Upper inner quadrant",
                        "Lower outer quadrant",
                        "Lower inner quadrant",
                        "Central",
                        "Retroareolar",
                        "1 o'clock",
                        "2 o'clock",
                        "3 o'clock",
                        "4 o'clock",
                        "5 o'clock",
                        "6 o'clock",
                        "7 o'clock",
                        "8 o'clock",
                        "9 o'clock",
                        "10 o'clock",
                        "11 o'clock",
                        "12 o'clock",
                    ],
                    key=f"{prefix}_specific_location",
                ),
            },
            child_value_options=[
                "Specify tumor site / location",
            ],
            key=f"{prefix}_site",
        ),

        conditional_radio_multiple(
            label="Histologic Type",
            options=[
                "Invasive carcinoma of no special type (ductal)",
                "No residual invasive carcinoma",
                nst_pattern,
                "Invasive lobular carcinoma, classic",
                lobular_variant,
                mixed_histologic_types,
                "Tubular carcinoma, pure or greater than 90%",
                (
                    "Invasive cribriform carcinoma, "
                    "pure or greater than 90%"
                ),
                "Mucinous carcinoma, pure or greater than 90%",
                (
                    "Invasive micropapillary carcinoma, "
                    "pure or greater than 90%"
                ),
                "Invasive apocrine carcinoma",
                "Metaplastic carcinoma, spindle cell",
                (
                    "Metaplastic carcinoma, with heterologous "
                    "differentiation / matrix production"
                ),
                "Metaplastic carcinoma, squamous cell",
                metaplastic_mixed,
                (
                    "Metaplastic carcinoma, favorable type, "
                    "low-grade adenosquamous"
                ),
                (
                    "Metaplastic carcinoma, favorable type, "
                    "low-grade fibromatosis-like"
                ),
                metaplastic_other,
                "Invasive solid papillary carcinoma",
                "Adenoid cystic carcinoma, classic",
                "Secretory carcinoma",
                other_histologic_type,
            ],
            conditional_fields={
                nst_pattern: text(
                    label="Specify Morphologic Pattern",
                    key=f"{prefix}_nst_morphologic_pattern",
                ),

                lobular_variant: text(
                    label="Specify Variant Pattern",
                    key=f"{prefix}_lobular_variant_pattern",
                ),

                mixed_histologic_types: text(
                    label=(
                        "Specify Histologic Types "
                        "and Percentages"
                    ),
                    key=f"{prefix}_mixed_histologic_types",
                ),

                metaplastic_mixed: text(
                    label="Specify Types and Percentages",
                    key=f"{prefix}_metaplastic_mixed_types",
                ),

                metaplastic_other: text(
                    label=(
                        "Specify Other Metaplastic "
                        "Carcinoma Type"
                    ),
                    key=f"{prefix}_metaplastic_other_type",
                ),

                other_histologic_type: text(
                    label="Specify Other Histologic Type",
                    key=f"{prefix}_other_histologic_type",
                ),
            },
            default="Invasive carcinoma of no special type (ductal)",
            key=f"{prefix}_histologic_type",
        ),

                    conditional_radio_multiple(
            label=(
                "Histologic Grade "
                "(Nottingham Histologic Score) "
                "(required only if applicable)"
            ),
            options=[
                (
                    "Not applicable "
                    "(no residual carcinoma or "
                    "microinvasion only)"
                ),
                "Nottingham Score",
            ],
            conditional_fields={
                "Nottingham Score": [
                    conditional_value(
                        label="Tubule Formation",
                        options=[
                            (
                                "Score 1"
                            ),
                            (
                                "Score 2"
                            ),
                            (
                                "Score 3"
                            ),
                            (
                                "Only microinvasion present "
                                "(not graded)"
                            ),
                            "Score cannot be determined",
                        ],
                        value_fields={
                            "Score cannot be determined": (
                                "Explain",
                                "",
                            ),
                        },
                        key=f"{prefix}_tubule_formation",
                    ),

                    conditional_value(
                        label="Nuclear Pleomorphism",
                        options=[
                            (
                                "Score 1"
                            ),
                            (
                                "Score 2"
                            ),
                            (
                                "Score 3"
                            ),
                            (
                                "Only microinvasion present "
                                "(not graded)"
                            ),
                            "Score cannot be determined",
                        ],
                        value_fields={
                            "Score cannot be determined": (
                                "Explain",
                                "",
                            ),
                        },
                        key=f"{prefix}_nuclear_pleomorphism",
                    ),

                    conditional_value(
                        label=(
                            "Mitotic Rate "
                            "(see Table 1 in Note E)"
                        ),
                        options=[
                            "Score 1",
                            "Score 2",
                            "Score 3",
                            (
                                "Only microinvasion present "
                                "(not graded)"
                            ),
                            "Score cannot be determined",
                        ],
                        value_fields={
                            "Score cannot be determined": (
                                "Explain",
                                "",
                            ),
                        },
                        key=f"{prefix}_mitotic_rate",
                    ),

                    conditional_value(
                        label="Overall Grade",
                        options=[
                            "Grade 1 (scores of 3, 4 or 5)",
                            "Grade 2 (scores of 6 or 7)",
                            "Grade 3 (scores of 8 or 9)",
                            (
                                "Only microinvasion present "
                                "(not graded)"
                            ),
                            "Score cannot be determined",
                        ],
                        value_fields={
                            "Score cannot be determined": (
                                "Explain",
                                "",
                            ),
                        },
                        key=f"{prefix}_overall_grade",
                    ),
                ],
            },
            key=f"{prefix}_histologic_grade",
        ),

        conditional_value(
            label="Tumor Size",
            options=[
                "No residual invasive carcinoma",
                (
                    "Microinvasion only "
                    "(less than or equal to 1 mm)"
                ),
                exact_tumor_size,
                tumor_size_cannot_be_determined,
            ],
            value_fields={
                exact_tumor_size: (
                    "Specify Exact Measurement",
                    " mm",
                ),
                tumor_size_cannot_be_determined: (
                    "Explain",
                    "",
                ),
            },
            key=f"{prefix}_tumor_size",
        ),

        *(
            [
                conditional_value(
                    label=(
                        "Size(s) and Location(s) of Additional "
                        "Foci in Millimeters (mm)"
                    ),
                    options=[
                        "Specify size(s) and location(s)",
                        "Cannot be determined",
                        "Not applicable",
                    ],
                    value_fields={
                        "Specify size(s) and location(s)": (
                            (
                                "Specify Size(s) and Location(s) "
                                "Using mm and Semicolons"
                            ),
                            "",
                        ),
                        "Cannot be determined": (
                            "Explain",
                            "",
                        ),
                    },
                    key=f"{prefix}_additional_foci",
                ),
            ]
            if include_additional_foci
            else []
        ),
    ]
    
    if numbered:
        return [
            text_group(
                label=f"Tumor {tumor_number}",
                prompt="Tumor Identifier",
                child_fields=characteristic_fields,
                key=f"{prefix}_identifier",
            )
        ]

    return characteristic_fields

def lymph_node_number_field(
    label: str,
    key: str,
    *,
    include_do_not_include: bool = False,
    include_not_applicable: bool = False,
) -> dict:
    """Create a lymph-node number field."""

    options = []

    if include_do_not_include:
        options.append("Do not include")

    if include_not_applicable:
        options.append("Not applicable ")

    options.extend(
        [
            "Exact number",
            "Other",
            "Cannot be determined",
        ]
    )

    return conditional_value(
        label=label,
        options=options,
        value_fields={
            "Exact number": (
                "Specify Exact Number",
                "",
            ),
            "Other": (
                "Specify Other",
                "",
            ),
            "Cannot be determined": (
                "Explain",
                "",
            ),
        },
        key=key,
    )


def lymph_node_measurement_field(
    label: str,
    key: str,
    *,
    exact_option: str = "Exact size",
) -> dict:
    """Create a nodal measurement field in millimeters."""

    return conditional_value(
        label=label,
        options=[
            exact_option,
            "Other",
            "Cannot be determined",
        ],
        value_fields={
            exact_option: (
                "Specify Measurement",
                " mm",
            ),
            "Other": (
                "Specify Other",
                "",
            ),
            "Cannot be determined": (
                "Explain",
                "",
            ),
        },
        key=key,
    )

ER_POSITIVE = (
    "Positive "
    "(greater than 10% of cells demonstrate nuclear positivity)"
)

ER_LOW_POSITIVE = (
    "Low Positive "
    "(1-10% of cells with nuclear positivity)"
)


def breast_biomarker_studies(
    key_prefix: str = "breast_biomarkers",
) -> list[dict]:
    """Create ER, PgR, HER2, and Ki-67 study fields."""

    return [
        conditional_radio_multiple(
            label="Biomarker Studies Performed On",
            options=[
                "Prior specimen",
                "Current specimen",
                "Do not include",
            ],
            conditional_fields={
                "Prior specimen": text(
                    label="Prior Case Number",
                    key=f"{key_prefix}_prior_case_number",
                ),
            },
            key=f"{key_prefix}_specimen_source",
        ),

        conditional_radio_multiple(
            label="Estrogen Receptor (ER) Status",
            options=[
                ER_POSITIVE,
                ER_LOW_POSITIVE,
                "Negative",
                "Cannot be determined",
            ],
            conditional_fields={
                ER_POSITIVE: radio(
                    label=(
                        "Percentage of Cells with Nuclear "
                        "Positivity for ER"
                    ),
                    options=[
                        "11-20%",
                        "21-30%",
                        "31-40%",
                        "41-50%",
                        "51-60%",
                        "61-70%",
                        "71-80%",
                        "81-90%",
                        "91-100%",
                    ],
                    key=f"{key_prefix}_er_percentage",
                ),

                "Cannot be determined": text(
                    label="Explain",
                    key=(
                        f"{key_prefix}_er_"
                        "cannot_be_determined"
                    ),
                ),
            },
            key=f"{key_prefix}_er_status",
        ),

        conditional_radio_multiple(
            label="Progesterone Receptor (PgR) Status",
            options=[
                "Positive",
                "Negative",
                "Cannot be determined",
            ],
            conditional_fields={
                "Positive": radio(
                    label=(
                        "Percentage of Cells with Nuclear "
                        "Positivity for PgR"
                    ),
                    options=[
                        "1-10%",
                        "11-20%",
                        "21-30%",
                        "31-40%",
                        "41-50%",
                        "51-60%",
                        "61-70%",
                        "71-80%",
                        "81-90%",
                        "91-100%",
                    ],
                    key=f"{key_prefix}_pgr_percentage",
                ),

                "Cannot be determined": text(
                    label="Explain",
                    key=(
                        f"{key_prefix}_pgr_"
                        "cannot_be_determined"
                    ),
                ),
            },
            key=f"{key_prefix}_pgr_status",
        ),

        radio(
            label="HER2 Status (by immunohistochemistry)",
            options=[
                "Negative (Score 0)",
                "Negative (Score 0+)",
                "Negative (Score 1+)",
                "Equivocal (Score 2+)",
                "Positive (Score 3+)",
            ],
            key=f"{key_prefix}_her2_ihc_status",
        ),

        radio(
            label="HER2 Status (by in situ hybridization)",
            options=[
                "Negative (not amplified)",
                "Positive (amplified)",
            ],
            key=f"{key_prefix}_her2_ish_status",
        ),

        radio(
            label="Percentage of Ki-67 Positive Nuclei",
            options=[
                "Favorable 1-10%",
                "Borderline 11-20%",
                "Unfavorable 21-30%",
                "Unfavorable 31-40%",
                "Unfavorable 41-50%",
                "Unfavorable 51-60%",
                "Unfavorable 61-70%",
                "Unfavorable 71-80%",
                "Unfavorable 81-90%",
                "Unfavorable 91-100%",
            ],
            key=f"{key_prefix}_ki67_percentage",
        ),
    ]

SYNOPTIC = [

    ("title", "CASE SUMMARY", "(INVASIVE CARCINOMA OF THE BREAST: Resection) Standard(s): AJCC 8"),

    ("section", "SPECIMEN"),

    conditional_value(
        label="Procedure",
        options=[
            "Lumpectomy",
            "Excisional biopsy",
            "Excision (less than total mastectomy, including lumpectomy and partial mastectomy)",
            "Total mastectomy (including nipple-sparing and skin-sparing mastectomy)",
            "Other",
            "Not specified",
        ],
        value_fields={
            "Other": (
                "Other Procedure",
                "",
            ),
        },
        key="procedure",
    ),

    radio(
        label="Specimen Laterality",
        options=[
            "Right",
            "Left",
            "Not specified",
        ],
        key="specimen_laterality",
    ),

        ("section", "TUMOR CHARACTERISTICS"),

    conditional_radio_multiple(
        label="Tumor Focality",
        options=[
            "Unifocal",
            "Multifocal",
            "No residual invasive carcinoma",
            "Cannot be determined",
        ],
        conditional_fields={
            "Unifocal": tumor_characteristics(
                1,
                numbered=False,
            ),

            "Multifocal": [

                number_of_foci("multifocal"),

                conditional_radio_multiple(
                    label="Multifocal Tumor Pattern",
                    options=[
                        SIMILAR_TUMOR_FOCI,
                        DIFFERENT_TUMOR_FOCI,
                        "Other (specify)",
                        "Cannot be determined (explain)",
                    ],
                    conditional_fields={
                        SIMILAR_TUMOR_FOCI: tumor_characteristics(
                            1,
                            numbered=False,
                            include_additional_foci=True,
                        ),

                        DIFFERENT_TUMOR_FOCI: (
                            conditional_radio_multiple(
                                label=(
                                    "Number of Distinct Tumor "
                                    "Characteristics Sections"
                                ),
                                options=[
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                ],
                                conditional_fields={
                                    str(count): (
                                        repeated_tumor_characteristics(
                                            count
                                        )
                                    )
                                    for count in range(2, 6)
                                },
                                default="2",
                                key=(
                                    "number_of_distinct_"
                                    "tumor_sections"
                                ),
                            )
                        ),

                        "Other (specify)": [
                            text(
                                label=(
                                    "Specify Other Multifocal "
                                    "Tumor Pattern"
                                ),
                                key=(
                                    "multifocal_pattern_other"
                                ),
                            ),
                            *tumor_characteristics(
                                1,
                                numbered=False,
                            ),
                        ],

                        "Cannot be determined (explain)": [
                            text(
                                label="Explain",
                                key=(
                                    "multifocal_pattern_"
                                    "cannot_be_determined"
                                ),
                            ),
                            *tumor_characteristics(
                                1,
                                numbered=False,
                            ),
                        ],
                    },
                    key="multifocal_tumor_pattern",
                ),

                
            ],

            "Cannot be determined": [
                text(
                    label="Explain",
                    key=(
                        "tumor_focality_"
                        "cannot_be_determined"
                    ),
                ),
            ],
        },
        key="tumor_focality",
    ),

    conditional_radio_multiple(
        label="Ductal Carcinoma In Situ (DCIS)",
        options=[
            "Not identified",
            "Present",
        ],
        conditional_fields={
            "Present": [
                checkbox_group(
                    label="Extent of DCIS",
                    options=[
                        "Admixed with invasive carcinoma",
                        "Extends beyond the invasive carcinoma",
                        "Separate from the invasive carcinoma",
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Admixed with invasive carcinoma": text(
                            label=(
                                "Specify DCIS as a Percentage "
                                "of Entire Tumor"
                            ),
                            suffix=" %",
                            key="dcis_percentage_of_entire_tumor",
                        ),

                        "Other": text(
                            label="Specify Other Extent of DCIS",
                            key="dcis_extent_other",
                        ),

                        "Cannot be determined": text(
                            label="Explain",
                            key="dcis_extent_cannot_be_determined",
                        ),
                    },
                    key="dcis_extent",
                ),

                conditional_radio_multiple(
                    label="Estimated Size of DCIS",
                    options=[
                        (
                            "Largest dimension of DCIS "
                            "in Millimeters (mm)"
                        ),
                        "Other",
                    ],
                    conditional_fields={
                        (
                            "Largest dimension of DCIS "
                            "in Millimeters (mm)"
                        ): text(
                            label="Specify Largest Dimension",
                            suffix=" mm",
                            key="dcis_largest_dimension",
                        ),

                        "Other": text(
                            label="Specify Other Estimated Size",
                            key="dcis_estimated_size_other",
                        ),
                    },
                    key="dcis_estimated_size",
                ),

                checkbox_group(
                    label="Architectural Pattern(s)",
                    options=[
                        "Do not include",
                        "Comedo",
                        "Cribriform",
                        "Micropapillary",
                        "Papillary",
                        "Solid",
                        "Solid papillary carcinoma in situ",
                        "Encapsulated papillary carcinoma in situ",
                        "Paget disease (DCIS involving nipple skin)",
                        "Other",
                    ],
                    conditional_fields={
                        "Other": text(
                            label="Specify Other Architectural Pattern",
                            key="dcis_architectural_pattern_other",
                        ),
                    },
                    exclusive_options=[
                        "Do not include",
                    ],
                    key="dcis_architectural_patterns",
                ),

                radio(
                    label="Nuclear Grade",
                    options=[
                        "Do not include",
                        "Grade I (low)",
                        "Grade II (intermediate)",
                        "Grade III (high)",
                    ],
                    key="dcis_nuclear_grade",
                ),

                conditional_radio_multiple(
                    label="Necrosis",
                    options=[
                        "Do not include",
                        "Not identified",
                        (
                            "Present, focal "
                            "(small foci or single cell necrosis)"
                        ),
                        (
                            "Present, central "
                            '(expansive "comedo" necrosis)'
                        ),
                        "Cannot be excluded",
                    ],
                    conditional_fields={
                        "Cannot be excluded": text(
                            label="Explain",
                            key="dcis_necrosis_cannot_be_excluded",
                        ),
                    },
                    key="dcis_necrosis",
                ),
            ],
        },
        key="dcis_status",
    ),

    checkbox_group(
        label="Additional Lesion(s)",
        options=[
            "Do not include",
            "Not identified",
            "Lobular carcinoma in situ, classic",
            "Lobular carcinoma in situ, pleomorphic",
            "Atypical lobular hyperplasia",
            "Atypical ductal hyperplasia",
            "Flat epithelial atypia",
            "Other",
        ],
        conditional_fields={
            
            "Other": text(
                label="Specify Other Additional Lesion",
                key="additional_lesion_other",
            ),
        },
        exclusive_options=[
            "Do not include",
            "Not identified",
        ],
        default="Do not include",
        key="additional_lesions",
    ),

    conditional_radio_multiple(
        label=(
            "Tumor Extent"
        ),
        options=[
            (
                "Not applicable "
                "(skin, nipple, and skeletal muscle are absent "
                "or uninvolved, and it is not necessary to "
                "document their presence)"
            ),
            (
                "Applicable "
                "(nipple, skin, or skeletal muscle are involved, "
                "or their presence should be documented)"
            ),
        ],
        conditional_fields={
            (
                "Applicable "
                "(nipple, skin, or skeletal muscle are involved, "
                "or their presence should be documented)"
            ): [
                checkbox_group(
                    label="Nipple Status",
                    options=[
                        "Do not include",
                        "Not present in specimen",
                        "Present and not involved",
                        "Paget's disease present",
                        "Involved by invasive carcinoma",
                        "DCIS in major lactiferous ducts present",
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other": text(
                            label="Specify Other Nipple Status",
                            key="nipple_status_other",
                        ),
                        "Cannot be determined": text(
                            label="Explain",
                            key="nipple_status_cannot_be_determined",
                        ),
                    },
                    exclusive_options=[
                        "Do not include",
                    ],
                    key="nipple_status",
                ),

                conditional_radio_multiple(
                    label="Skin Status",
                    options=[
                        "Do not include",
                        "Not present in specimen",
                        "Present and not involved",
                        (
                            "Carcinoma directly invades into the dermis "
                            "or epidermis without macroscopic skin "
                            "ulceration (this does not change the "
                            "T classification)"
                        ),
                        (
                            "Carcinoma directly invades into the dermis "
                            "or epidermis with macroscopic skin ulceration "
                            "(classified as T4b)"
                        ),
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other": text(
                            label="Specify Other Skin Status",
                            key="skin_status_other",
                        ),
                        "Cannot be determined": text(
                            label="Explain",
                            key="skin_status_cannot_be_determined",
                        ),
                    },
                    key="skin_status",
                ),

                conditional_radio_multiple(
                    label="Macroscopic Skin Satellite Foci",
                    options=[
                        "Do not include",
                        "Not identified",
                        "Present (T4b)",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Cannot be determined": text(
                            label="Explain",
                            key=(
                                "macroscopic_skin_satellite_foci_"
                                "cannot_be_determined"
                            ),
                        ),
                    },
                    key="macroscopic_skin_satellite_foci",
                ),

                conditional_radio_multiple(
                    label="Skeletal Muscle",
                    options=[
                        "Do not include",
                        "Not present in specimen",
                        "Present and not involved",
                        "Carcinoma invades skeletal muscle",
                        (
                            "Carcinoma invades into the chest wall "
                            "deep to pectoralis muscle "
                            "(classified as T4a)"
                        ),
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other": text(
                            label="Specify Other Skeletal Muscle Status",
                            key="skeletal_muscle_other",
                        ),
                        "Cannot be determined": text(
                            label="Explain",
                            key=(
                                "skeletal_muscle_"
                                "cannot_be_determined"
                            ),
                        ),
                    },
                    key="skeletal_muscle_status",
                ),
            ],
        },
        key="tumor_extent",
    ),

    conditional_radio_multiple(
        label="Lymphatic and / or Vascular Invasion",
        options=[
            "Not identified",
            (
                "Present, focal "
                "(limited to one to two vessels in one block)"
            ),
            (
                "Present, extensive "
                "(greater than two vessels in one block or "
                "present in two or more blocks)"
            ),
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Other": text(
                label=(
                    "Specify Other Lymphatic and / or "
                    "Vascular Invasion"
                ),
                key="lymphovascular_invasion_other",
            ),
            "Cannot be determined": text(
                label="Explain",
                key=(
                    "lymphovascular_invasion_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="lymphovascular_invasion",
    ),

    text(
        label=(
            "Lymphatic and / or Vascular "
            "Invasion Comment"
        ),
        key="lymphovascular_invasion_comment",
    ),

    conditional_radio_multiple(
        label=(
            "Dermal Lymphatic and / or Vascular Invasion "
        ),
        options=[
            "Do not include",
            "Not applicable (no skin present)",
            "Not identified",
            "Present",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Other": text(
                label=(
                    "Specify Other Dermal Lymphatic "
                    "and / or Vascular Invasion"
                ),
                key="dermal_lymphovascular_invasion_other",
            ),
            "Cannot be determined": text(
                label="Explain",
                key=(
                    "dermal_lymphovascular_invasion_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="dermal_lymphovascular_invasion",
    ),

    checkbox_group(
        label="Microcalcifications",
        options=[
            "Do not include",
            "Not identified",
            "Present in DCIS",
            "Present in invasive carcinoma",
            "Present in non-neoplastic tissue",
            "Other",
        ],
        conditional_fields={
            "Other": text(
                label="Specify Other Microcalcifications",
                key="microcalcifications_other",
            ),
        },
        exclusive_options=[
            "Do not include",
            "Not identified",
        ],
        key="microcalcifications",
    ),

    ("section", "TREATMENT EFFECT"),

    conditional_radio_multiple(
        label="Treatment Effect in Breast",
        options=[
            "No known presurgical therapy",
            (
                "No definite response to presurgical therapy "
                "in the invasive carcinoma"
            ),
            (
                "Evidence of response to presurgical therapy "
                "in the invasive carcinoma"
            ),
            (
                "No residual invasive carcinoma is present "
                "in the breast after presurgical therapy"
            ),
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Other": text(
                label="Specify Other Treatment Effect in Breast",
                key="treatment_effect_breast_other",
            ),
            "Cannot be determined": text(
                label="Explain",
                key=(
                    "treatment_effect_breast_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="treatment_effect_breast",
    ),

    conditional_radio_multiple(
        label="Treatment Effect in Lymph Node(s)",
        options=[
            "Do not include",
            "Not applicable ",
            (
                "No definite response to presurgical therapy "
                "in metastatic carcinoma"
            ),
            (
                "Metastatic carcinoma present with evidence "
                "of response to presurgical therapy"
            ),
            (
                "No lymph node metastases. Fibrous scarring or "
                "histiocytic aggregates, possibly related to prior "
                "lymph node metastases with pathologic complete response"
            ),
            (
                "No lymph node metastases and no fibrous scarring "
                "or histiocytic aggregates in the nodes"
            ),
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": text(
                label="Explain",
                key=(
                    "treatment_effect_lymph_nodes_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="treatment_effect_lymph_nodes",
    ),

    conditional_radio_multiple(
        label="RCB Score and Class",
        options=[
            "Do not include",
            "Not applicable ",
            "Applicable",
        ],
        conditional_fields={
            "Applicable": [
                display_link(
                    label="Residual Cancer Burden Calculator",
                    link_text="Open MD Anderson RCB Calculator",
                    url=(
                        "http://www3.mdanderson.org/app/medcalc/"
                        "index.cfm?pagename=jsconvert3"
                    ),
                ),

                text(
                    label=(
                        "Greatest Dimension of Primary Tumor Bed Area "
                        "in Millimeters (mm) "
                        "(involved by residual invasive carcinoma)"
                    ),
                    suffix=" mm",
                    key="rcb_tumor_bed_greatest_dimension",
                ),

                text(
                    label=(
                        "Second Greatest Dimension of Primary Tumor "
                        "Bed Area in Millimeters (mm)"
                    ),
                    suffix=" mm",
                    key="rcb_tumor_bed_second_dimension",
                ),

                text(
                    label=(
                        "Percentage of Overall Cancer Cellularity "
                        "(in the area measured above)"
                    ),
                    suffix=" %",
                    key="rcb_overall_cancer_cellularity",
                ),

                text(
                    label=(
                        "Percentage of Cancer that is "
                        "In Situ Disease"
                    ),
                    suffix=" %",
                    key="rcb_percentage_in_situ",
                ),

                text(
                    label="Number of Positive Lymph Nodes",
                    key="rcb_number_positive_lymph_nodes",
                ),

                text(
                    label=(
                        "Diameter of Largest Nodal Metastasis "
                        "in Millimeters (mm)"
                    ),
                    suffix=" mm",
                    key="rcb_largest_nodal_metastasis",
                ),

                text(
                    label="Residual Cancer Burden Score",
                    key="rcb_score",
                ),

                radio(
                    label="Residual Cancer Burden Class",
                    options=[
                        "RCB-0 (pCR)",
                        "RCB-I",
                        "RCB-II",
                        "RCB-III",
                    ],
                    key="rcb_class",
                ),
            ],
        },
        key="rcb_section_status",
    ),

    ("section", "MARGINS"),

    conditional_radio_multiple(
        label="Final Margin Status for Invasive Carcinoma",
        options=[
            (
                "Not applicable "
                "(no residual invasive carcinoma in specimen)"
            ),
            (
                "All final margins greater than 2 mm "
                "from invasive carcinoma"
            ),
            invasive_margin_within_2_mm,
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            invasive_margin_within_2_mm: [
                margin_location_field(
                    label=(
                        "Margin(s) Involved by "
                        "Invasive Carcinoma (at ink)"
                    ),
                    specify_option="Specify involved margins",
                    key="invasive_margin_involved",
                ),

                margin_location_field(
                    label=(
                        "Margin(s) Less than 1 mm from "
                        "Invasive Carcinoma (but not at ink)"
                    ),
                    key="invasive_margin_less_than_1_mm",
                ),

                margin_location_field(
                    label=(
                        "Margin(s) 1 to 2 mm from "
                        "Invasive Carcinoma"
                    ),
                    key="invasive_margin_1_to_2_mm",
                ),

                margin_location_field(
                    label=(
                        "Margin(s) Greater than 2 mm from "
                        "Invasive Carcinoma"
                    ),
                    key="invasive_margin_greater_than_2_mm",
                ),
            ],

            "Other": text(
                label="Specify Other Final Margin Status",
                key="final_margin_status_invasive_other",
            ),

            "Cannot be determined": text(
                label="Explain",
                key=(
                    "final_margin_status_invasive_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="final_margin_status_invasive",
    ),

    conditional_radio_multiple(
        label="Final Margin Status for DCIS",
        options=[
            (
                "Not applicable "
                "(no residual DCIS in specimen)"
            ),
            "All final margins greater than 2 mm from DCIS",
            dcis_margin_within_2_mm,
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            dcis_margin_within_2_mm: [
                margin_location_field(
                    label="Margin(s) Involved by DCIS (at ink)",
                    key="dcis_margin_involved",
                ),

                margin_location_field(
                    label=(
                        "Margin(s) Less than 1 mm from DCIS "
                        "(but not at ink)"
                    ),
                    key="dcis_margin_less_than_1_mm",
                ),

                margin_location_field(
                    label="Margin(s) 1 to 2 mm from DCIS",
                    key="dcis_margin_1_to_2_mm",
                ),

                margin_location_field(
                    label="Margin(s) Greater than 2 mm from DCIS",
                    key="dcis_margin_greater_than_2_mm",
                ),
            ],

            "Other": text(
                label="Specify Other Final Margin Status for DCIS",
                key="final_margin_status_dcis_other",
            ),

            "Cannot be determined": text(
                label="Explain",
                key=(
                    "final_margin_status_dcis_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="final_margin_status_dcis",
    ),

    ("section", "REGIONAL LYMPH NODES"),

    conditional_radio_multiple(
        label="Regional Lymph Node Status",
        options=[
            (
                "Not applicable "
                "(no regional lymph nodes submitted or found)"
            ),
            "Regional lymph nodes present",
        ],
        conditional_fields={
            "Regional lymph nodes present": [
                conditional_radio_multiple(
                    label="Regional Lymph Node Tumor Status",
                    options=[
                        (
                            "All regional lymph nodes "
                            "negative for tumor"
                        ),
                        (
                            "Tumor present in regional "
                            "lymph node(s)"
                        ),
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        (
                            "Tumor present in regional "
                            "lymph node(s)"
                        ): [
                            lymph_node_number_field(
                                label=(
                                    "Number of Lymph Nodes with "
                                    "Macrometastases "
                                    "(greater than 2 mm)"
                                ),
                                key=(
                                    "lymph_nodes_"
                                    "with_macrometastases"
                                ),
                            ),

                            lymph_node_number_field(
                                label=(
                                    "Number of Lymph Nodes with "
                                    "Micrometastases "
                                    "(greater than 0.2 mm to 2 mm "
                                    "and / or greater than 200 cells)"
                                ),
                                key=(
                                    "lymph_nodes_"
                                    "with_micrometastases"
                                ),
                            ),

                            lymph_node_number_field(
                                label=(
                                    "Number of Lymph Nodes with "
                                    "Isolated Tumor Cells "
                                    "(0.2 mm or less or "
                                    "200 cells or less)"
                                ),
                                include_do_not_include=True,
                                include_not_applicable=True,
                                key=(
                                    "lymph_nodes_with_"
                                    "isolated_tumor_cells"
                                ),
                            ),

                            lymph_node_number_field(
                                label=(
                                    "Total Number of Positive "
                                    "Macroscopic and Microscopic "
                                    "Lymph Nodes Counted Towards "
                                    "pN Category"
                                ),
                                key=(
                                    "total_positive_lymph_nodes_"
                                    "counted_towards_pn"
                                ),
                            ),

                            lymph_node_measurement_field(
                                label=(
                                    "Size of Largest Nodal "
                                    "Metastatic Deposit"
                                ),
                                key=(
                                    "largest_nodal_"
                                    "metastatic_deposit"
                                ),
                            ),

                            conditional_radio_multiple(
                                label="Extranodal Extension (ENE)",
                                options=[
                                    "Not identified",
                                    "Present",
                                    "Other",
                                    "Cannot be determined",
                                ],
                                conditional_fields={
                                    "Present": [
                                        lymph_node_measurement_field(
                                            label=(
                                                "Largest Measurement "
                                                "of Extranodal Extension"
                                            ),
                                            exact_option=(
                                                "Exact measurement"
                                            ),
                                            key=(
                                                "largest_measurement_"
                                                "of_extranodal_extension"
                                            ),
                                        ),

                                        lymph_node_number_field(
                                            label=(
                                                "Number of Lymph Nodes "
                                                "with Extranodal Extension"
                                            ),
                                            key=(
                                                "number_of_lymph_nodes_"
                                                "with_extranodal_extension"
                                            ),
                                        ),
                                    ],

                                    "Other": text(
                                        label=(
                                            "Specify Other Extranodal "
                                            "Extension Finding"
                                        ),
                                        key=(
                                            "extranodal_extension_other"
                                        ),
                                    ),

                                    "Cannot be determined": text(
                                        label="Explain",
                                        key=(
                                            "extranodal_extension_"
                                            "cannot_be_determined"
                                        ),
                                    ),
                                },
                                key="extranodal_extension",
                            ),
                        ],

                        "Other": text(
                            label=(
                                "Specify Other Regional Lymph "
                                "Node Tumor Status"
                            ),
                            key=(
                                "regional_lymph_node_"
                                "tumor_status_other"
                            ),
                        ),

                        "Cannot be determined": text(
                            label="Explain",
                            key=(
                                "regional_lymph_node_"
                                "tumor_status_cannot_be_determined"
                            ),
                        ),
                    },
                    key="regional_lymph_node_tumor_status",
                ),

                lymph_node_number_field(
                    label=(
                        "Total Number of Lymph Nodes Examined "
                        "(sentinel and non-sentinel)"
                    ),
                    key="total_lymph_nodes_examined",
                ),
            ],
        },
        key="regional_lymph_node_status",
    ),

    ("section", "DISTANT METASTASIS"),

    checkbox_group(
        label=(
            "Distant Site(s) Involved"
        ),
        options=[
            "Not applicable ",
            "Non-regional lymph node(s)",
            "Lung",
            "Liver",
            "Bone",
            "Brain",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Non-regional lymph node(s)": text(
                label="Specify Non-regional Lymph Node Site(s)",
                key="distant_metastasis_nonregional_lymph_nodes",
            ),
            "Other": text(
                label="Specify Other Distant Site",
                key="distant_metastasis_other",
            ),

            "Cannot be determined": text(
                label="Comment",
                key="distant_metastasis_cannot_be_determined",
            ),
        },
        exclusive_options=[
            "Not applicable ",
        ],
        key="distant_sites_involved",
    ),

    ("section", "SPECIAL STUDIES"),

    *breast_biomarker_studies(),

    conditional_radio_multiple(
        label="Immunohistochemistry",
        options=[
            "Do not include",
            "Include",
        ],
        conditional_fields={
            "Include": text(
                label="Immunohistochemistry Results / Comment",
                key="special_studies_immunohistochemistry_comment",
            ),
        },
        child_value_options=[
            "Include",
        ],
        key="special_studies_immunohistochemistry",
    ),

    conditional_radio_multiple(
        label="Other Special Studies",
        options=[
            "Do not include",
            "Include",
        ],
        conditional_fields={
            "Include": text(
                label="Specify Other Special Studies",
                key="special_studies_other_comment",
            ),
        },
        child_value_options=[
            "Include",
        ],
        key="special_studies_other",
    ),

    ("section", "pTNM CLASSIFICATION (AJCC 8th Edition)"),

    option_toggle(
        label="Show pTNM definitions in table",
        key=TNM_DEFINITIONS_KEY,
        default=False,
    ),

    radio_toggle(
        label="Modified Classification",
        options=MODIFIED_CLASSIFICATION_OPTIONS,
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_modified_classification",
    ),

    radio_toggle(
        label="pT Category",
        options=PT_CATEGORY_OPTIONS,
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_pt_category",
    ),

    radio_toggle(
        label="T Suffix",
        options=T_SUFFIX_OPTIONS,
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_t_suffix",
    ),

    radio_toggle(
        label="pN Category",
        options=PN_CATEGORY_OPTIONS,
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_pn_category",
    ),

    radio_toggle(
        label="N Suffix",
        options=N_SUFFIX_OPTIONS,
        session_key=TNM_DEFINITIONS_KEY,
        key="breast_n_suffix",
    ),

    conditional_radio_multiple(
        label="pM Category",
        options=[
            "Do not include",
            (
                "Not applicable - pM cannot be determined "
                "from the submitted specimen(s)"
            ),
            (
                "pM1: Histologically proven metastases "
                "larger than 0.2 mm"
            ),
        ],
        conditional_fields={
            (
                "pM1: Histologically proven metastases "
                "larger than 0.2 mm"
            ): text(
                label=(
                    "Specify Case Number(s) with Metastasis "
                    "(if from a previous procedure)"
                ),
                key="breast_pm1_metastasis_case_numbers",
            ),
        },
        key="breast_pm_category",
    ),

]