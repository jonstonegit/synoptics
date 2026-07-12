from helpers import (
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
}

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


]