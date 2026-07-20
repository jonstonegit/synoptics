from synoptic_engine import (
    option_toggle,
    radio,
    radio_toggle,
    radio_other,
    text,
    conditional_radio_multiple,
    conditional_radio_other,
    conditional_value,
    checkbox_group,
    field_label,
    handle_exclusive_checkbox,
)

DISPLAY_NAME = "Prostate, Resection"

HIDDEN_TABLE_VALUES = {
    "Via percentage",
    "Via dimension",
    "Via percentage; Via dimension",
    "Do not include additional findings section",
    "Do not include special studies section",
}

def nodal_laterality(site_key: str):
    return checkbox_group(
        label="Laterality (select all that apply)",
        options=[
            "Right",
            "Left",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    label="Comment",
                    key=f"{site_key}_laterality_cannot_be_determined",
                ),
            ],
        },
        exclusive_options=[
            "Cannot be determined",
        ],
        key=f"{site_key}_laterality",
    )


def positive_nodal_site_fields(site_key: str):
    return [
        text(
            label="Number of Lymph Nodes with Tumor at This Site",
            key=f"{site_key}_positive_node_count",
        ),
        nodal_laterality(site_key),
    ]


def regional_node_summary_fields():
    return [
        conditional_value(
            label="Number of Lymph Nodes Examined",
            options=[
                "Exact number",
                "At least",
                "Other",
                "Cannot be determined",
            ],
            value_fields={
                "Exact number": (
                    "Specify exact number",
                    "",
                ),
                "At least": (
                    "Specify minimum number",
                    "",
                ),
                "Other": (
                    "Specify",
                    "",
                ),
                "Cannot be determined": (
                    "Comment",
                    "",
                ),
            },
            key="number_of_lymph_nodes_examined",
        ),
    ]


def positive_regional_node_fields():
    return [
        conditional_value(
            label="Number of Lymph Nodes with Tumor",
            options=[
                "Exact number",
                "At least",
                "Other",
                "Cannot be determined",
            ],
            value_fields={
                "Exact number": (
                    "Specify exact number",
                    "",
                ),
                "At least": (
                    "Specify minimum number",
                    "",
                ),
                "Other": (
                    "Specify",
                    "",
                ),
                "Cannot be determined": (
                    "Comment",
                    "",
                ),
            },
            key="number_of_lymph_nodes_with_tumor",
        ),

        checkbox_group(
            label="Nodal Site(s) with Tumor (select all that apply)",
            options=[
                "Hypogastric",
                "Obturator",
                "Internal iliac",
                "External iliac",
                "Iliac, NOS",
                "Pelvic, NOS",
                "Lateral sacral",
                "Presacral",
                "Promontory",
                "Sacral, NOS",
                "Other",
            ],
            conditional_fields={
                "Hypogastric": positive_nodal_site_fields(
                    "hypogastric"
                ),
                "Obturator": positive_nodal_site_fields(
                    "obturator"
                ),
                "Internal iliac": positive_nodal_site_fields(
                    "internal_iliac"
                ),
                "External iliac": positive_nodal_site_fields(
                    "external_iliac"
                ),
                "Iliac, NOS": positive_nodal_site_fields(
                    "iliac_nos"
                ),
                "Pelvic, NOS": positive_nodal_site_fields(
                    "pelvic_nos"
                ),
                "Lateral sacral": positive_nodal_site_fields(
                    "lateral_sacral"
                ),
                "Presacral": positive_nodal_site_fields(
                    "presacral"
                ),
                "Promontory": positive_nodal_site_fields(
                    "promontory"
                ),
                "Sacral, NOS": positive_nodal_site_fields(
                    "sacral_nos"
                ),
                "Other": [
                    text(
                        label="Specify Other Nodal Site",
                        key="other_positive_nodal_site",
                    ),
                ],
            },
            key="nodal_sites_with_tumor",
        ),

        conditional_value(
            label="Size of Largest Nodal Metastatic Deposit",
            options=[
                "Exact size",
                "At least",
                "Greater than",
                "Less than",
                "Other",
                "Cannot be determined",
            ],
            value_fields={
                "Exact size": (
                    "Specify exact size",
                    " cm",
                ),
                "At least": (
                    "Specify minimum size",
                    " cm",
                ),
                "Greater than": (
                    "Specify size",
                    " cm",
                ),
                "Less than": (
                    "Specify size",
                    " cm",
                ),
                "Other": (
                    "Specify",
                    "",
                ),
                "Cannot be determined": (
                    "Comment",
                    "",
                ),
            },
            key="largest_nodal_metastatic_deposit_size",
        ),

        text(
            label="Nodal Site with Largest Metastatic Deposit",
            key="largest_metastatic_deposit_nodal_site",
        ),

        conditional_value(
            label="Size of Largest Lymph Node with Tumor",
            options=[
                "Exact size",
                "At least",
                "Greater than",
                "Less than",
                "Other",
                "Cannot be determined",
            ],
            value_fields={
                "Exact size": (
                    "Specify exact size",
                    " cm",
                ),
                "At least": (
                    "Specify minimum size",
                    " cm",
                ),
                "Greater than": (
                    "Specify size",
                    " cm",
                ),
                "Less than": (
                    "Specify size",
                    " cm",
                ),
                "Other": (
                    "Specify",
                    "",
                ),
                "Cannot be determined": (
                    "Comment",
                    "",
                ),
            },
            key="largest_lymph_node_with_tumor_size",
        ),

        text(
            label="Largest Lymph Node with Tumor (specify site)",
            key="largest_lymph_node_with_tumor_site",
        ),

        conditional_value(
            label="Extranodal Extension",
            options=[
                "Not identified",
                "Present",
                "Cannot be determined",
                "Other",
            ],
            value_fields={
                "Cannot be determined": (
                    "Comment",
                    "",
                ),
                "Other": (
                    "Specify",
                    "",
                ),
            },
            key="extranodal_extension",
        ),

        *regional_node_summary_fields(),
    ]

epe_location_field = checkbox_group(
        label="Location of Extraprostatic Extension (select all that apply)",
        options=[
            "Right apical",
            "Right bladder neck",
            "Right anterior",
            "Right lateral",
            "Right posterolateral (neurovascular bundle)",
            "Right posterior",
            "Left apical",
            "Left bladder neck",
            "Left anterior",
            "Left lateral",
            "Left posterolateral (neurovascular bundle)",
            "Left posterior",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Other": text(
                "Other location(s)",
                key="epe_location_other",
            ),
            "Cannot be determined": text(
                "Comment",
                key="epe_location_cannot_be_determined_explanation",
            ),
        },
        exclusive_options=[
            "Cannot be determined",
        ],
        key="epe_location",
    ),

SYNOPTIC = [

    ("title", "CASE SUMMARY", "(PROSTATE GLAND: Radical Prostatectomy) Standard(s): AJCC-UICC 8"),

    ("section", "SPECIMEN"),

    radio_other(
        "Procedure",
        [
            "Radical prostatectomy",
            "Not specified",
        ],
    ),

    ("section", "TUMOR"),

    radio_other(
        "Histologic Type",
        [
            "Acinar adenocarcinoma, conventional (usual)",
            "Acinar adenocarcinoma, signet-ring-like cell",
            "Acinar adenocarcinoma, pleomorphic giant cell",
            "Acinar adenocarcinoma, sarcomatoid",
            "Acinar adenocarcinoma, prostatic intraepithelial neoplasia-like",
            "Intraductal carcinoma",
            "Ductal adenocarcinoma",
            "Adenosquamous carcinoma",
            "Squamous cell carcinoma",
            "Basal cell (adenoid cystic) carcinoma",
            "Adenocarcinoma with neuroendocrine differentiation",
            "Well-differentiated neuroendocrine tumor",
            "Small cell neuroendocrine carcinoma",
            "Large cell neuroendocrine carcinoma",
            "Carcinoma, type cannot be determined",
        ],
    ),

    ("section", "HISTOLOGIC GRADE"),

    conditional_radio_multiple(
        "Grade",
        [
            "Grade group 1 (Gleason Score 3 + 3 = 6)",
            "Grade group 2 (Gleason Score 3 + 4 = 7)",
            "Grade group 3 (Gleason Score 4 + 3 = 7)",
            "Grade group 4 (Gleason Score 4 + 4 = 8)",
            "Grade group 4 (Gleason Score 3 + 5 = 8)",
            "Grade group 4 (Gleason Score 5 + 3 = 8)",
            "Grade group 5 (Gleason Score 4 + 5 = 9)",
            "Grade group 5 (Gleason Score 5 + 4 = 9)",
            "Grade group 5 (Gleason Score 5 + 5 = 10)",
            "Cannot be assessed",
            "Not applicable",
        ],
        conditional_fields={
            "Grade group 2 (Gleason Score 3 + 4 = 7)": [
                radio(
                    "Minor Tertiary Pattern 5 (less than 5%)",
                    [
                        "Not applicable / not identified",
                        "Present",
                    ],
                    key="grade_group_2_tertiary_pattern_5",
                ),
                radio(
                    "Percentage of Pattern 4",
                    [
                        "Less than or equal to 5%",
                        "6 - 10%",
                        "11 - 20%",
                        "21 - 30%",
                        "31 - 40%",
                        "Greater than 40%",
                    ],
                    key="grade_group_2_pattern_4_percentage",
                ),
            ],

            "Grade group 3 (Gleason Score 4 + 3 = 7)": [
                radio(
                    "Minor Tertiary Pattern 5 (less than 5%)",
                    [
                        "Not applicable / not identified",
                        "Present",
                    ],
                    key="grade_group_3_tertiary_pattern_5",
                ),
                radio(
                    "Percentage of Pattern 4",
                    [
                        "Less than 61%",
                        "61 - 70%",
                        "71 - 80%",
                        "81 - 90%",
                        "Greater than 90%",
                    ],
                    key="grade_group_3_pattern_4_percentage",
                ),
            ],

            "Grade group 4 (Gleason Score 4 + 4 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_44_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_44_pattern_5",
                ),
            ],

            "Grade group 4 (Gleason Score 3 + 5 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_35_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_35_pattern_5",
                ),
            ],

            "Grade group 4 (Gleason Score 5 + 3 = 8)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_4_53_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_4_53_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 4 + 5 = 9)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_45_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_45_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 5 + 4 = 9)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_54_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_54_pattern_5",
                ),
            ],

            "Grade group 5 (Gleason Score 5 + 5 = 10)": [
                text(
                    "Percentage of Pattern 4",
                    suffix="%",
                    key="grade_5_55_pattern_4",
                ),
                text(
                    "Percentage of Pattern 5",
                    suffix="%",
                    key="grade_5_55_pattern_5",
                ),
            ],

            "Cannot be assessed": text(
                "Specify",
                key="grade_cannot_be_assessed_comment",
            ),

            "Not applicable": text(
                "Specify",
                key="grade_not_applicable_comment",
            ),
        },
    ),

    conditional_radio_multiple(
        "Intraductal Carcinoma (IDC)",
        [
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Present": radio(
                "IDC Incorporated into Grade",
                [
                    "Yes",
                    "No",
                ],
                key="idc_incorporated_into_grade",
            ),
            "Cannot be determined": [
                text(
                    "Comment",
                    key="IDC_cannot_be_determined",
                ),
            ],
        },
        key="intraductal_carcinoma",
    ),

    conditional_radio_multiple(
        "Cribriform Glands",
        [
            "Not applicable",
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    "Comment",
                    key="cribriform_glands_cannot_be_determined",
                ),
            ],
        },
    ),

    checkbox_group(
        label="Treatment Effect",
        options=[
            "No known presurgical therapy",
            "Not identified",
            "Radiation therapy effect present",
            "Hormonal therapy effect present",
            "Other therapy effect(s) present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Radiation therapy effect present": text(
                "Radiation therapy effect",
                key="radiation_therapy_effect_detail",
            ),
            "Hormonal therapy effect present": text(
                "Hormonal therapy effect",
                key="hormonal_therapy_effect_detail",
            ),
            "Other therapy effect(s) present": text(
                "Other therapy effect(s)",
                key="other_therapy_effect_detail",
            ),
            "Cannot be determined": text(
                "Comment",
                key="treatment_effect_cannot_be_determined_reason",
            ),
        },
        default="No known presurgical therapy",
        exclusive_options=[
            "No known presurgical therapy",
            "Not identified",
        ],
        key="treatment_effect",
    ),

    (
    "section",
    "TUMOR QUANTITATION",
    ),

    checkbox_group(
        label="Tumor Quantitation",
        options=[
            "Via percentage",
            "Via dimension",
        ],
        conditional_fields={
            "Via percentage": conditional_radio_multiple(
                label="Estimated Percentage of Prostate Involved by Tumor",
                options=[
                    "Less than 1%",
                    "1 - 5%",
                    "6 - 10%",
                    "11 - 20%",
                    "21 - 30%",
                    "31 - 40%",
                    "41 - 50%",
                    "51 - 60%",
                    "61 - 70%",
                    "71 - 80%",
                    "81 - 90%",
                    "Greater than 90%",
                    "Cannot be determined",
                ],
                conditional_fields={
                    "Cannot be determined": text(
                        "Comment",
                        key="tumor_percentage_cannot_be_determined_explanation",
                    ),
                },
                key="estimated_percentage_prostate_involved",
            ),

            "Via dimension": [
                text(
                    "Greatest Dimension of Dominant Nodule in mm",
                    suffix=" mm",
                    key="dominant_nodule_greatest_dimension",
                ),
                text(
                    "Additional Dimensions of Dominant Nodule in mm",
                    suffix=" mm",
                    key="dominant_nodule_additional_dimensions",
                ),
                text(
                    "Location of Dominant Nodule",
                    key="dominant_nodule_location",
                ),
            ],
        },
        key="tumor_quantitation_method",
    ),

    conditional_radio_multiple(
        label="Extraprostatic Extension (EPE)",
        options=[
            "Not identified",
            "Present, focal",
            "Present, nonfocal",
            "Cannot be determined",
        ],
        conditional_fields={
            "Present, focal": epe_location_field,
            "Present, nonfocal": epe_location_field,
            "Cannot be determined": text(
                "Comment",
                key="epe_cannot_be_determined_explanation",
            ),
        },
        key="extraprostatic_extension",
    ),

    conditional_value(
        label="Urinary Bladder Neck Invasion",
        options=[
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        value_fields={
            "Cannot be determined": (
                "Comment",
                "",
            ),
        },
        key="urinary_bladder_neck_invasion",
    ),

    radio(
        label="Seminal Vesicle Invasion",
        options=[
            "Not identified",
            "Present, right",
            "Present, left",
            "Present, bilateral",
            "Present, laterality cannot be determined",
            "No seminal vesicle present",
        ],
        key="seminal_vesicle_invasion",
    ),

    conditional_value(
    label="Lymphatic and / or Vascular Invasion",
    options=[
        "Not identified",
        "Present",
        "Cannot be determined",
    ],
    value_fields={
        "Cannot be determined": (
            "Comment",
            "",
        ),
    },
    key="lymphatic_or_vascular_invasion",
),

    conditional_value(
        label="Perineural Invasion",
        options=[
            "Do not include",
            "Not identified",
            "Present",
        ],
        value_fields={
            "Present": (
                "Specify",
                "",
            ),
        },
        key="perineural_invasion",
    ),

    ("section", "MARGINS"),

    conditional_radio_multiple(
        label="Margin Status",
        options=[
            "All margins negative for invasive carcinoma",
            "Invasive carcinoma present at margin",
            "Cannot be assessed",
        ],
        conditional_fields={
            "Cannot be assessed": [
                text(
                    label="C0mment",
                    key="margin_status_cannot_be_assessed_explanation",
                ),
            ],

            "Invasive carcinoma present at margin": [
                conditional_radio_multiple(
                    label="Linear Length of Margin(s) Involved by Carcinoma",
                    options=[
                        "Do not include",
                        "Specify exact length in Millimeters (mm)",
                        "Less than 3 mm (limited)",
                        "Greater than or equal to 3 mm (non-limited)",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Specify exact length in Millimeters (mm)": [
                            text(
                                label="Exact Length",
                                suffix=" mm",
                                key="margin_involvement_exact_length",
                            ),
                        ],

                        "Cannot be determined": [
                            text(
                                label="Comment",
                                key="margin_length_cannot_be_determined_explanation",
                            ),
                        ],
                    },
                    key="linear_length_of_involved_margin",
                ),

                radio(
                    label="Focality of Margin Involvement",
                    options=[
                        "Do not include",
                        "Unifocal",
                        "Multifocal",
                    ],
                    key="margin_involvement_focality",
                ),

                checkbox_group(
                    label=(
                        "Margin(s) Involved by Invasive Carcinoma "
                    ),
                    options=[
                        "Right apical",
                        "Right bladder neck",
                        "Right anterior",
                        "Right lateral",
                        "Right posterolateral (neurovascular bundle)",
                        "Right posterior",
                        "Left apical",
                        "Left bladder neck",
                        "Left anterior",
                        "Left lateral",
                        "Left posterolateral (neurovascular bundle)",
                        "Left posterior",
                        "Other(s)",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other(s)": [
                            text(
                                label="Specify Other Margin(s)",
                                key="other_involved_margins",
                            ),
                        ],

                        "Cannot be determined": [
                            text(
                                label="Comment",
                                key="involved_margins_cannot_be_determined",
                            ),
                        ],
                    },
                    exclusive_options=[
                        "Cannot be determined",
                    ],
                    key="margins_involved_by_invasive_carcinoma",
                ),

                conditional_radio_multiple(
                    label=(
                        "Margin Involvement by Invasive Carcinoma in "
                        "Area of Extraprostatic Extension (EPE)"
                    ),
                    options=[
                        "Do not include",
                        "Not identified",
                        "Present",
                    ],
                    conditional_fields={
                        "Present": [
                            text(
                                label=(
                                    "Margin(s) Involved by Invasive "
                                    "Carcinoma in Area of EPE"
                                ),
                                key="margins_involved_in_area_of_epe",
                            ),
                        ],
                    },
                    key="margin_involvement_in_area_of_epe",
                ),

                checkbox_group(
                    label=(
                        "Gleason Pattern at Margin(s) Involved by "
                        "Carcinoma (Note K) (select all that apply)"
                    ),
                    options=[
                        "Do not inlcude",
                        "Pattern 3",
                        "Pattern 4",
                        "Pattern 5",
                    ],
                    key="gleason_pattern_at_involved_margin",
                    default="Do not inlcude"
                ),
            ],
        },
        key="margin_status",
    ),

    ("section", "REGIONAL LYMPH NODES"),

    conditional_radio_multiple(
        label="Regional Lymph Node Status",
        options=[
            "Not applicable (no regional lymph nodes submitted or found)",
            "All regional lymph nodes negative for tumor",
            "Tumor present in regional lymph node(s)",
        ],
        conditional_fields={
            "All regional lymph nodes negative for tumor": (
                regional_node_summary_fields()
            ),

            "Tumor present in regional lymph node(s)": (
                positive_regional_node_fields()
            ),
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
            "Nonregional lymph node(s)",
            "Bone",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Nonregional lymph node(s)": [
                text(
                    label="Specify Nonregional Lymph Node Site(s)",
                    key="distant_nonregional_lymph_node_sites",
                ),
            ],

            "Bone": [
                text(
                    label="Specify Bone Site(s)",
                    key="distant_bone_sites",
                ),
            ],

            "Other": [
                text(
                    label="Specify Other Distant Site(s)",
                    key="other_distant_metastatic_sites",
                ),
            ],

            "Cannot be determined": [
                text(
                    label="Comment",
                    key="distant_metastasis_cannot_be_determined",
                ),
            ],
        },
        exclusive_options=[
            "Not applicable ",
            "Cannot be determined",
        ],
        default="Not applicable ",
        key="distant_sites_involved",
    ),
    
    ("section", "ADDITIONAL FINDINGS"),

    checkbox_group(
        label="Additional Findings",
        options=[
            "Do not include additional findings section",
            "None identified",
            "Atypical intraductal proliferation (AIP)",
            "High-grade prostatic intraepithelial neoplasia (PIN)",
            "Atypical adenomatous hyperplasia (adenosis)",
            "Nodular prostatic hyperplasia",
            "Inflammation",
            "Other",
        ],
        conditional_fields={
            "High-grade prostatic intraepithelial neoplasia (PIN)": [
                text(
                    label="Specify",
                    key="high_grade_pin_details",
                ),
            ],
            "Inflammation": [
                text(
                    label="Specify Type of Inflammation",
                    key="inflammation_type",
                ),
            ],
            "Other": [
                text(
                    label="Specify Other Additional Finding",
                    key="other_additional_finding",
                ),
            ],
        },
        exclusive_options=[
            "Do not include additional findings section",
            "None identified",
        ],
        key="additional_findings",
        default="Do not include additional findings section",
    ),

    ("section", "SPECIAL STUDIES"),

    conditional_radio_multiple(
        label="Special Studies",
        options=[
            "Do not include special studies section",
            "Immunohistochemistry",
            "Other",
        ],
        conditional_fields={
            "Immunohistochemistry": text(
                label="Immunohistochemical Studies",
                key="ancillary_studies_immunohistochemistry",
            ),
            "Other": text(
                label="Other Ancillary Studies",
                key="ancillary_studies_other",
            ),
        },
        key="ancillary_studies",
    ),


    ("section", "pTNM CLASSIFICATION (AJCC 8th Edition)"),

    option_toggle(
        label="Include full TNM definitions in table",
        key="show_full_tnm",
        default=False,
    ),

    radio(
    label="Modified Classification",
    options=[
        "Do not include",
        "Not applicable",
        "y (post-neoadjuvant therapy)",
        "r (recurrence)",
    ],
    key="modified_classification",
),

radio_toggle(
    label="pT Category",
    session_key="show_full_tnm",
    options=[
        (
            "pT2: Organ confined",
            "pT2",
        ),
        (
            "pT3a: Extraprostatic extension or microscopic invasion of bladder neck",
            "pT3a",
        ),
        (
            "pT3b: Tumor invades seminal vesicle(s)",
            "pT3b",
        ),
        (
            "pT3: Subcategory cannot be determined",
            "pT3",
        ),
        (
            """pT4: Tumor is fixed or invades adjacent structures other 
            than seminal vesicles, such as external sphincter, rectum, 
            bladder, levator muscles, and/or pelvic wall""",
            "pT4",
        ),
    ],
),

radio(
    label="T Suffix",
    options=[
        "Do not include",
        "Not applicable",
        "(m) Multiple primary synchronous tumors in a single organ",
    ],
    key="t_suffix",
),

radio_toggle(
    label="pN Category",
    session_key="show_full_tnm",
    options=[
        (
            "pN not assigned (No nodes submitted or found)",
            "pN not assigned (No nodes submitted or found)",
        ),
        (
            "pN not assigned: Cannot be determined based on available pathological information",
            "pN not assigned",
        ),
        (
            "pN0: No positive regional lymph nodes",
            "pN0",
        ),
        (
            "pN1: Metastasis in regional lymph node(s)",
            "pN1",
        ),
    ],
),

radio_toggle(
    label="pM Category",
    session_key="show_full_tnm",
    options=[
        (
            "Do not include",
            "Do not include",
        ),
        (
            "Not applicable: pM cannot be determined from the submitted specimen(s)",
            "pM not applicable",
        ),
        (
            "pM1a: Metastasis in nonregional lymph node(s)",
            "pM1a",
        ),
        (
            "pM1b: Metastasis in bone(s)",
            "pM1b",
        ),
        (
            "pM1c: Metastasis at other site(s), with or without bone disease",
            "pM1c",
        ),
    ],
),

]