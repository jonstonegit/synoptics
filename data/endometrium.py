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

DISPLAY_NAME = "Endometrium"

HIDDEN_TABLE_VALUES = {
    "Do not include",
    "Do not include additional findings section",
    "Do not include special studies section",
}

MMR_PROTEINS = [
    "MLH1",
    "PMS2",
    "MSH2",
    "MSH6",
]

UTERUS_TNM_DEFINITIONS_KEY = "show_uterus_tnm_definitions"


UTERUS_PT_CATEGORY_OPTIONS = [
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
        (
            "pT1a: Tumor limited to the endometrium or "
            "invading less than half the myometrium"
        ),
        "pT1a",
    ),
    (
        (
            "pT1b: Tumor invading one half or more "
            "of the myometrium"
        ),
        "pT1b",
    ),
    (
        "pT1 (subcategory cannot be determined)",
        "pT1",
    ),
    (
        (
            "pT2: Tumor invading the stromal connective "
            "tissue of the cervix but not extending beyond "
            "the uterus. Does not include endocervical "
            "glandular involvement."
        ),
        "pT2",
    ),
    (
        (
            "pT3a: Tumor involving the serosa and / or "
            "adnexa (direct extension or metastasis)"
        ),
        "pT3a",
    ),
    (
        (
            "pT3b: Vaginal involvement "
            "(direct extension or metastasis) "
            "or parametrial involvement"
        ),
        "pT3b",
    ),
    (
        "pT3 (subcategory cannot be determined)",
        "pT3",
    ),
    (
        (
            "pT4: Tumor invading bladder mucosa and / or "
            "bowel mucosa (bullous edema is not sufficient "
            "to classify a tumor as T4)"
        ),
        "pT4",
    ),
]

UTERUS_FIGO_DEFINITIONS_KEY = "show_uterus_figo_definitions"


UTERUS_FIGO_2009_OPTIONS = [
    (
        "Do not include",
        "Do not include",
    ),
    (
        "I: Tumor confined to the corpus uteri",
        "I",
    ),
    (
        (
            "IA: No or less than half "
            "myometrial invasion"
        ),
        "IA",
    ),
    (
        (
            "IB: Invasion equal to or more than "
            "half of the myometrium"
        ),
        "IB",
    ),
    (
        (
            "II: Tumor invades cervical stroma, "
            "but does not extend beyond the uterus"
        ),
        "II",
    ),
    (
        (
            "III: Local and / or regional spread "
            "of the tumor"
        ),
        "III",
    ),
    (
        (
            "IIIA: Tumor invades the serosa of the "
            "corpus uteri and / or adnexae"
        ),
        "IIIA",
    ),
    (
        (
            "IIIB: Vaginal and / or "
            "parametrial involvement"
        ),
        "IIIB",
    ),
    (
        (
            "IIIC: Metastases to pelvic and / or "
            "para-aortic lymph nodes"
        ),
        "IIIC",
    ),
    (
        "IIIC1: Positive pelvic nodes",
        "IIIC1",
    ),
    (
        (
            "IIIC2: Positive para-aortic nodes "
            "with or without positive pelvic lymph nodes"
        ),
        "IIIC2",
    ),
    (
        (
            "IV: Tumor invades bladder and / or bowel "
            "mucosa, and / or distant metastases"
        ),
        "IV",
    ),
    (
        (
            "IVA: Tumor invasion of bladder "
            "and / or bowel mucosa"
        ),
        "IVA",
    ),
    (
        (
            "IVB: Distant metastasis, including "
            "intra-abdominal metastases and / or "
            "inguinal nodes"
        ),
        "IVB",
    ),
]


UTERUS_FIGO_2023_OPTIONS = [
    (
        "Do not include",
        "Do not include",
    ),
    (
        (
            "I: Confined to the uterine "
            "corpus and ovary"
        ),
        "I",
    ),
    (
        (
            "IA: Disease limited to the endometrium "
            "or non-aggressive histological type, "
            "including low-grade endometrioid carcinoma, "
            "with invasion of less than half of the "
            "myometrium and no or focal lymphovascular "
            "space involvement, or good-prognosis disease"
        ),
        "IA",
    ),
    (
        (
            "IA1: Non-aggressive histological type "
            "limited to an endometrial polyp or "
            "confined to the endometrium"
        ),
        "IA1",
    ),
    (
        (
            "IA2: Non-aggressive histological types "
            "involving less than half of the myometrium "
            "with no or focal lymphovascular space "
            "involvement"
        ),
        "IA2",
    ),
    (
        (
            "IA3: Low-grade endometrioid carcinomas "
            "limited to the uterus and ovary"
        ),
        "IA3",
    ),
    (
        (
            "IAm (POLEmut): POLE-mutated endometrial "
            "carcinoma confined to the uterine corpus "
            "or with cervical extension, regardless "
            "of the degree of lymphovascular space "
            "involvement or histological type"
        ),
        "IAm (POLEmut)",
    ),
    (
        (
            "IB: Non-aggressive histological types "
            "with invasion of half or more of the "
            "myometrium and with no or focal "
            "lymphovascular space involvement"
        ),
        "IB",
    ),
    (
        (
            "IC: Aggressive histological types limited "
            "to a polyp or confined to the endometrium"
        ),
        "IC",
    ),
    (
        (
            "II: Invasion of cervical stroma without "
            "extrauterine extension, or with substantial "
            "lymphovascular space involvement, or "
            "aggressive histological types with "
            "myometrial invasion"
        ),
        "II",
    ),
    (
        (
            "IIA: Invasion of the cervical stroma of "
            "non-aggressive histological types"
        ),
        "IIA",
    ),
    (
        (
            "IIB: Substantial lymphovascular space "
            "involvement of non-aggressive "
            "histological types"
        ),
        "IIB",
    ),
    (
        (
            "IIC: Aggressive histological types "
            "with any myometrial involvement"
        ),
        "IIC",
    ),
    (
        (
            "IICm (p53abn): p53-abnormal endometrial "
            "carcinoma confined to the uterine corpus "
            "with any myometrial invasion, with or "
            "without cervical invasion, and regardless "
            "of the degree of lymphovascular space "
            "involvement or histological type"
        ),
        "IICm (p53abn)",
    ),
    (
        (
            "III: Local and / or regional spread of "
            "the tumor of any histological subtype"
        ),
        "III",
    ),
    (
        (
            "IIIA: Invasion of uterine serosa, adnexa, "
            "or both by direct extension or metastasis"
        ),
        "IIIA",
    ),
    (
        (
            "IIIA1: Spread to ovary or fallopian tube, "
            "except when meeting stage IA3 criteria"
        ),
        "IIIA1",
    ),
    (
        (
            "IIIA2: Involvement of uterine subserosa "
            "or spread through the uterine serosa"
        ),
        "IIIA2",
    ),
    (
        (
            "IIIB: Metastasis or direct spread to the "
            "vagina and / or parametria or pelvic "
            "peritoneum"
        ),
        "IIIB",
    ),
    (
        (
            "IIIB1: Metastasis or direct spread to "
            "the vagina and / or the parametria"
        ),
        "IIIB1",
    ),
    (
        (
            "IIIB2: Metastasis to the "
            "pelvic peritoneum"
        ),
        "IIIB2",
    ),
    (
        (
            "IIIC: Metastasis to pelvic or para-aortic "
            "lymph nodes or both"
        ),
        "IIIC",
    ),
    (
        (
            "IIIC1: Metastasis to the "
            "pelvic lymph nodes"
        ),
        "IIIC1",
    ),
    (
        (
            "IIIC1i: Micrometastasis "
            "to pelvic lymph nodes"
        ),
        "IIIC1i",
    ),
    (
        (
            "IIIC1ii: Macrometastasis "
            "to pelvic lymph nodes"
        ),
        "IIIC1ii",
    ),
    (
        (
            "IIIC2: Metastasis to para-aortic lymph "
            "nodes up to the renal vessels, with or "
            "without metastasis to the pelvic lymph nodes"
        ),
        "IIIC2",
    ),
    (
        (
            "IIIC2i: Micrometastasis to para-aortic "
            "lymph nodes up to the renal vessels, "
            "with or without metastasis to pelvic nodes"
        ),
        "IIIC2i",
    ),
    (
        (
            "IIIC2ii: Macrometastasis to para-aortic "
            "lymph nodes up to the renal vessels, "
            "with or without metastasis to pelvic nodes"
        ),
        "IIIC2ii",
    ),
    (
        (
            "IV: Spread to the bladder mucosa and / or "
            "intestinal mucosa and / or distant metastasis"
        ),
        "IV",
    ),
    (
        (
            "IVA: Invasion of the bladder mucosa "
            "and / or intestine or bowel mucosa"
        ),
        "IVA",
    ),
    (
        (
            "IVB: Abdominal peritoneal metastasis "
            "beyond the pelvis"
        ),
        "IVB",
    ),
    (
        (
            "IVC: Distant metastasis, including "
            "metastasis to extra-abdominal or "
            "intra-abdominal lymph nodes above the "
            "renal vessels, lungs, liver, brain, or bone"
        ),
        "IVC",
    ),
]


UTERUS_T_SUFFIX_OPTIONS = [
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


UTERUS_PN_CATEGORY_OPTIONS = [
    (
        "pN not assigned (no nodes submitted or found)",
        "pN not assigned",
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
        "pN0: No regional lymph node metastasis",
        "pN0",
    ),
    (
        (
            "pN0(i+): Isolated tumor cells in regional "
            "lymph node(s) no greater than 0.2 mm"
        ),
        "pN0(i+)",
    ),
    (
        (
            "pN1mi: Regional lymph node metastasis "
            "(greater than 0.2 mm but not greater than "
            "2.0 mm in diameter) to pelvic lymph nodes"
        ),
        "pN1mi",
    ),
    (
        (
            "pN1a: Regional lymph node metastasis "
            "(greater than 2.0 mm in diameter) "
            "to pelvic lymph nodes"
        ),
        "pN1a",
    ),
    (
        "pN1 (subcategory cannot be determined)",
        "pN1",
    ),
    (
        (
            "pN2mi: Regional lymph node metastasis "
            "(greater than 0.2 mm but not greater than "
            "2.0 mm in diameter) to para-aortic lymph "
            "nodes, with or without positive pelvic "
            "lymph nodes"
        ),
        "pN2mi",
    ),
    (
        (
            "pN2a: Regional lymph node metastasis "
            "(greater than 2.0 mm in diameter) to "
            "para-aortic lymph nodes, with or without "
            "positive pelvic lymph nodes"
        ),
        "pN2a",
    ),
    (
        "pN2 (subcategory cannot be determined)",
        "pN2",
    ),
]


UTERUS_N_SUFFIX_OPTIONS = [
    (
        "Not applicable",
        "Not applicable",
    ),
    (
        "(sn) Sentinel node procedure",
        "(sn)",
    ),
    (
        "(f) FNA or core biopsy",
        "(f)",
    ),
]


UTERUS_PM_CATEGORY_OPTIONS = [
    (
        (
            "Not applicable - pM cannot be determined "
            "from the submitted specimen(s)"
        ),
        "Not applicable",
    ),
    (
        (
            "pM1: Distant metastasis "
            "(includes metastasis to inguinal lymph nodes, "
            "intraperitoneal disease, lung, liver, or bone)"
        ),
        "pM1",
    ),
]




def mmr_msi_fields() -> list[dict]:
    """Create MMR immunohistochemistry and MSI testing fields."""

    mmr_loss = "Loss of nuclear MMR protein expression"

    mmr_subclonal_loss = (
        "Subclonal loss of nuclear MMR protein expression"
    )

    return [
        conditional_radio_multiple(
            label="MMR Immunohistochemistry",
            options=[
                "Not performed",
                (
                    "Intact nuclear expression of MLH1, "
                    "PMS2, MSH2 and MSH6"
                ),
                mmr_loss,
                mmr_subclonal_loss,
                "MMR immunohistochemistry pending",
            ],
            conditional_fields={
                mmr_loss: checkbox_group(
                    label="MMR Protein(s) with Loss of Expression",
                    options=MMR_PROTEINS,
                    key="mmr_proteins_with_loss",
                ),

                mmr_subclonal_loss: checkbox_group(
                    label=(
                        "MMR Protein(s) with Subclonal "
                        "Loss of Expression"
                    ),
                    options=MMR_PROTEINS,
                    key="mmr_proteins_with_subclonal_loss",
                ),
            },
            child_value_options=[
                mmr_loss,
                mmr_subclonal_loss,
            ],
            key="mmr_immunohistochemistry",
        ),

        radio(
            label="Microsatellite Instability (MSI) Testing",
            options=[
                "Not performed",
                "MSI-Stable (MSS)",
                "MSI-Low (MSI-L)",
                "MSI-High (MSI-H)",
                "MSI testing pending",
            ],
            key="msi_testing",
        ),

        conditional_radio_multiple(
            label=(
                "MSI Testing Method "
                "(required only if applicable)"
            ),
            options=[
                "Not applicable (not performed)",
                "Polymerase chain reaction",
                "Next generation sequencing",
                "MSI testing pending",
                "Cannot be determined",
            ],
            conditional_fields={
                "Cannot be determined": text(
                    label="Explain",
                    key="msi_testing_method_cannot_be_determined",
                ),
            },
            key="msi_testing_method",
        ),
    ]


def p53_fields() -> list[dict]:
    """Create p53 immunohistochemistry and TP53 testing fields."""

    subclonal_abnormal = (
        "Subclonal abnormal (mutated) expression"
    )

    return [
        conditional_radio_multiple(
            label="p53 Immunohistochemistry",
            options=[
                "Not performed",
                "Normal (wild-type) expression",
                "Abnormal (mutated) expression",
                (
                    "Overexpression "
                    "(strong, diffuse nuclear expression)"
                ),
                (
                    "Null "
                    "(complete lack of nuclear and cytoplasmic "
                    "expression; internal positive control present)"
                ),
                (
                    "Cytoplasmic staining "
                    "(with or without nuclear expression)"
                ),
                subclonal_abnormal,
                "p53 immunohistochemistry pending",
            ],
            conditional_fields={
                subclonal_abnormal: radio(
                    label="Subclonal Abnormal Expression Pattern",
                    options=[
                        (
                            "Overexpression "
                            "(strong, diffuse nuclear expression)"
                        ),
                        (
                            "Null "
                            "(complete lack of nuclear and "
                            "cytoplasmic expression; internal "
                            "positive control present)"
                        ),
                        (
                            "Cytoplasmic staining "
                            "(with or without nuclear expression)"
                        ),
                    ],
                    key="p53_subclonal_abnormal_pattern",
                ),
            },
            key="p53_immunohistochemistry",
        ),

        conditional_radio_multiple(
            label="TP53 Mutation Testing",
            options=[
                "Not performed",
                "Wild-type",
                "Mutated",
                "Cannot be determined",
            ],
            conditional_fields={
                "Mutated": text(
                    label="Specify TP53 Mutation",
                    key="tp53_mutation_specify",
                ),

                "Cannot be determined": text(
                    label="Explain",
                    key="tp53_mutation_cannot_be_determined",
                ),
            },
            child_value_options=[
                "Mutated",
            ],
            key="tp53_mutation_testing",
        ),
    ]

def uterine_margin_sites(
    label: str,
    key: str,
) -> dict:
    """Create a multi-select uterine margin site field."""

    return checkbox_group(
        label=label,
        options=[
            "Ectocervical",
            "Vaginal cuff",
            "Parametrial",
            "Paracervical",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Ectocervical": text(
                label="Specify Ectocervical Location, if possible",
                key=f"{key}_ectocervical_location",
            ),

            "Vaginal cuff": text(
                label="Specify Vaginal Cuff Location, if possible",
                key=f"{key}_vaginal_cuff_location",
            ),

            "Parametrial": text(
                label="Specify Parametrial Location, if possible",
                key=f"{key}_parametrial_location",
            ),

            "Paracervical": text(
                label="Specify Paracervical Location, if possible",
                key=f"{key}_paracervical_location",
            ),

            "Other": text(
                label="Specify Other Margin",
                key=f"{key}_other",
            ),

            "Cannot be determined": text(
                label="Explain",
                key=f"{key}_cannot_be_determined",
            ),
        },
        exclusive_options=[
            "Cannot be determined",
        ],
        key=key,
    )

def nodal_count_field(
    label: str,
    key: str,
    *,
    include_not_applicable: bool = False,
) -> dict:
    """Create a lymph-node count field."""

    options = []

    if include_not_applicable:
        options.append("Not applicable")

    options.extend(
        [
            "Exact number",
            "At least",
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
            "At least": (
                "Specify Minimum Number",
                "",
            ),
            "Cannot be determined": (
                "Explain",
                "",
            ),
        },
        key=key,
    )


def nodal_metastasis_size_field(
    label: str,
    key: str,
) -> dict:
    """Create a nodal metastasis measurement field."""

    return conditional_value(
        label=label,
        options=[
            "Specify exact size",
            "Less than",
            "Greater than",
            "Cannot be determined",
        ],
        value_fields={
            "Specify exact size": (
                "Specify Exact Size",
                " mm",
            ),
            "Less than": (
                "Specify Measurement",
                " mm",
            ),
            "Greater than": (
                "Specify Measurement",
                " mm",
            ),
            "Cannot be determined": (
                "Explain",
                "",
            ),
        },
        key=key,
    )


def nodal_laterality_field(
    label: str,
    key: str,
) -> dict:
    """Create a multi-select nodal laterality field."""

    return checkbox_group(
        label=label,
        options=[
            "Right sentinel",
            "Right non-sentinel",
            "Left sentinel",
            "Left non-sentinel",
            "Cannot be determined",
        ],
        conditional_fields={
            "Right sentinel": text(
                label="Specify Right Sentinel Finding",
                key=f"{key}_right_sentinel",
            ),
            "Right non-sentinel": text(
                label="Specify Right Non-sentinel Finding",
                key=f"{key}_right_non_sentinel",
            ),
            "Left sentinel": text(
                label="Specify Left Sentinel Finding",
                key=f"{key}_left_sentinel",
            ),
            "Left non-sentinel": text(
                label="Specify Left Non-sentinel Finding",
                key=f"{key}_left_non_sentinel",
            ),
            "Cannot be determined": text(
                label="Explain",
                key=f"{key}_cannot_be_determined",
            ),
        },
        exclusive_options=[
            "Cannot be determined",
        ],
        key=key,
    )

def pelvic_positive_node_fields() -> list[dict]:
    """Create fields for metastatic pelvic lymph nodes."""

    return [
        nodal_count_field(
            label=(
                "Total Number of Pelvic Nodes with "
                "Macrometastasis (greater than 2 mm) "
                "(sentinel and non-sentinel)"
            ),
            key="pelvic_nodes_macrometastasis_total",
        ),

        nodal_count_field(
            label=(
                "Number of Pelvic Sentinel Nodes "
                "with Macrometastasis"
            ),
            key="pelvic_sentinel_nodes_macrometastasis",
        ),

        nodal_count_field(
            label=(
                "Total Number of Pelvic Nodes with "
                "Micrometastasis "
                "(greater than 0.2 mm up to 2 mm and / or "
                "greater than 200 cells) "
                "(sentinel and non-sentinel)"
            ),
            key="pelvic_nodes_micrometastasis_total",
        ),

        nodal_count_field(
            label=(
                "Number of Pelvic Sentinel Nodes "
                "with Micrometastasis"
            ),
            key="pelvic_sentinel_nodes_micrometastasis",
        ),

        nodal_count_field(
            label=(
                "Total Number of Pelvic Nodes with "
                "Isolated Tumor Cells "
                "(less than or equal to 0.2 mm, or "
                "200 cells or less)"
            ),
            include_not_applicable=True,
            key="pelvic_nodes_isolated_tumor_cells_total",
        ),

        nodal_count_field(
            label=(
                "Number of Pelvic Sentinel Nodes "
                "with Isolated Tumor Cells"
            ),
            key="pelvic_sentinel_nodes_isolated_tumor_cells",
        ),

        nodal_laterality_field(
            label="Laterality of Pelvic Node(s) with Tumor",
            key="pelvic_nodes_with_tumor_laterality",
        ),

        nodal_metastasis_size_field(
            label=(
                "Size of Largest Pelvic Nodal "
                "Metastatic Deposit"
            ),
            key="largest_pelvic_nodal_metastatic_deposit",
        ),
    ]

def para_aortic_positive_node_fields() -> list[dict]:
    """Create fields for metastatic para-aortic lymph nodes."""

    return [
        nodal_count_field(
            label=(
                "Total Number of Para-aortic Nodes with "
                "Macrometastasis (greater than 2 mm) "
                "(sentinel and non-sentinel)"
            ),
            key="para_aortic_nodes_macrometastasis_total",
        ),

        nodal_count_field(
            label=(
                "Number of Para-aortic Sentinel Nodes "
                "with Macrometastasis"
            ),
            key="para_aortic_sentinel_nodes_macrometastasis",
        ),

        nodal_count_field(
            label=(
                "Total Number of Para-aortic Nodes with "
                "Micrometastasis "
                "(greater than 0.2 mm up to 2 mm and / or "
                "greater than 200 cells) "
                "(sentinel and non-sentinel)"
            ),
            key="para_aortic_nodes_micrometastasis_total",
        ),

        nodal_count_field(
            label=(
                "Number of Para-aortic Sentinel Nodes "
                "with Micrometastasis"
            ),
            key="para_aortic_sentinel_nodes_micrometastasis",
        ),

        nodal_count_field(
            label=(
                "Total Number of Para-aortic Nodes with "
                "Isolated Tumor Cells "
                "(less than or equal to 0.2 mm, or "
                "200 cells or less)"
            ),
            include_not_applicable=True,
            key="para_aortic_nodes_isolated_tumor_cells_total",
        ),

        nodal_count_field(
            label=(
                "Number of Para-aortic Sentinel Nodes "
                "with Isolated Tumor Cells"
            ),
            key=(
                "para_aortic_sentinel_nodes_"
                "isolated_tumor_cells"
            ),
        ),

        nodal_laterality_field(
            label=(
                "Laterality of Para-aortic "
                "Node(s) with Tumor"
            ),
            key="para_aortic_nodes_with_tumor_laterality",
        ),

        nodal_metastasis_size_field(
            label=(
                "Size of Largest Para-aortic Nodal "
                "Metastatic Deposit"
            ),
            key=(
                "largest_para_aortic_nodal_"
                "metastatic_deposit"
            ),
        ),
    ]



SYNOPTIC = [

    ("section", "SPECIMEN"),

    checkbox_group(
        label="Procedure",
        options=[
            "Total hysterectomy",
            "Supracervical hysterectomy",
            "Radical hysterectomy",
            "Hysterectomy",
            "Bilateral salpingo-oophorectomy",
            "Right salpingo-oophorectomy",
            "Left salpingo-oophorectomy",
            "Salpingo-oophorectomy, side not specified",
            "Right oophorectomy",
            "Left oophorectomy",
            "Oophorectomy, side not specified",
            "Bilateral salpingectomy",
            "Right salpingectomy",
            "Left salpingectomy",
            "Salpingectomy, side not specified",
            "Vaginal cuff resection",
            "Omentectomy",
            "Peritoneal biopsy(ies)",
            "Peritoneal / pelvic washing",
            "Other",
        ],
        conditional_fields={
            "Other": text(
                label="Specify Other Procedure",
                key="procedure_other",
            ),
        },
        key="procedure",
    ),

    conditional_radio_multiple(
        label="Specimen Integrity",
        options=[
            "Do not include",
            "Intact",
            "Opened",
            "Morcellated",
            "Other",
        ],
        conditional_fields={
            "Other": text(
                label="Specify Other Specimen Integrity",
                key="specimen_integrity_other",
            ),
        },
        child_value_options=[
            "Other",
        ],
        key="specimen_integrity",
    ),

    ("section", "TUMOR"),

    conditional_radio_multiple(
        label="Tumor Size",
        options=[
            "Do not include",
            (
                "Greatest gross dimension "
                "(if mass) in Centimeters (cm)"
            ),
            (
                "Greatest microscopic dimension "
                "(if no mass) in Centimeters (cm)"
            ),
            "Cannot be determined",
        ],
        conditional_fields={
            (
                "Greatest gross dimension "
                "(if mass) in Centimeters (cm)"
            ): [
                text(
                    label="Greatest Gross Dimension",
                    suffix=" cm",
                    key="tumor_size_gross_greatest_dimension",
                ),
                text(
                    label="Additional Dimension 1",
                    suffix=" cm",
                    key="tumor_size_gross_additional_dimension_1",
                ),
                text(
                    label="Additional Dimension 2",
                    suffix=" cm",
                    key="tumor_size_gross_additional_dimension_2",
                ),
            ],

            (
                "Greatest microscopic dimension "
                "(if no mass) in Centimeters (cm)"
            ): [
                text(
                    label="Greatest Microscopic Dimension",
                    suffix=" cm",
                    key="tumor_size_microscopic_greatest_dimension",
                ),
                text(
                    label="Additional Dimension 1",
                    suffix=" cm",
                    key=(
                        "tumor_size_microscopic_"
                        "additional_dimension_1"
                    ),
                ),
                text(
                    label="Additional Dimension 2",
                    suffix=" cm",
                    key=(
                        "tumor_size_microscopic_"
                        "additional_dimension_2"
                    ),
                ),
            ],

            "Cannot be determined": text(
                label="Explain",
                key="tumor_size_cannot_be_determined",
            ),
        },
        child_value_options=[
            (
                "Greatest gross dimension "
                "(if mass) in Centimeters (cm)"
            ),
            (
                "Greatest microscopic dimension "
                "(if no mass) in Centimeters (cm)"
            ),
        ],
        key="tumor_size",
    ),

    conditional_radio_multiple(
        label="Histologic Type",
        options=[
            "Endometrioid carcinoma",
            "Serous carcinoma",
            "Clear cell carcinoma",
            "Dedifferentiated carcinoma",
            "Undifferentiated carcinoma",
            "Carcinosarcoma",
            "Mesonephric-like adenocarcinoma",
            "Squamous cell carcinoma",
            "Gastric (gastrointestinal)-type carcinoma",
            "Mixed carcinoma",
            "Small cell neuroendocrine carcinoma",
            "Large cell neuroendocrine carcinoma",
            "Other histologic type not listed",
        ],
        conditional_fields={
            "Mixed carcinoma": text(
                label="Specify Types and Percentages",
                key="histologic_type_mixed_types_percentages",
            ),

            "Other histologic type not listed": text(
                label="Specify Other Histologic Type",
                key="histologic_type_other",
            ),
        },
        child_value_options=[
            "Mixed carcinoma",
            "Other histologic type not listed",
        ],
        key="histologic_type",
    ),

    conditional_radio_multiple(
        label="Histologic Grade",
        options=[
            "FIGO grade 1 (endometrioid carcinoma)",
            "FIGO grade 2 (endometrioid carcinoma)",
            "FIGO grade 3 (endometrioid carcinoma)",
            "High-grade (non-endometrioid carcinoma)",
            "Other",
        ],
        conditional_fields={
            "Other": text(
                label="Specify Other Histologic Grade",
                key="histologic_grade_other",
            ),
        },
        child_value_options=[
            "Other",
        ],
        key="histologic_grade",
    ),

    checkbox_group(
        label="Molecular Type",
        options=[
            "Do not include",
            (
                "Mismatch Repair (MMR) / "
                "Microsatellite Instability (MSI) Status"
            ),
            "p53 Status",
        ],
        conditional_fields={
            (
                "Mismatch Repair (MMR) / "
                "Microsatellite Instability (MSI) Status"
            ): mmr_msi_fields(),

            "p53 Status": p53_fields(),
        },
        key="molecular_type",
    ),

    conditional_radio_multiple(
        label="Myometrial Invasion",
        options=[
            "Not applicable",
            "Not identified",
            "Present, inner half (less than 50%)",
            (
                "Present, outer half "
                "(greater than or equal to 50%)"
            ),
            "Cannot be determined",
        ],
        conditional_fields={
            "Present, inner half (less than 50%)": [
                text(
                    label="Specify Percentage",
                    suffix=" %",
                    key="myometrial_invasion_inner_half_percentage",
                ),
                text(
                    label="Myometrial Invasion Comment",
                    key="myometrial_invasion_inner_half_comment",
                ),
            ],

            (
                "Present, outer half "
                "(greater than or equal to 50%)"
            ): [
                text(
                    label="Specify Percentage",
                    suffix=" %",
                    key="myometrial_invasion_outer_half_percentage",
                ),
                text(
                    label="Myometrial Invasion Comment",
                    key="myometrial_invasion_outer_half_comment",
                ),
            ],

            "Cannot be determined": text(
                label="Explain",
                key="myometrial_invasion_cannot_be_determined",
            ),
        },
        key="myometrial_invasion",
    ),

    conditional_radio_multiple(
        label="Adenomyosis",
        options=[
            "Do not include",
            "Not identified",
            "Present, uninvolved by carcinoma",
            "Present, involved by carcinoma",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": text(
                label="Explain",
                key="adenomyosis_cannot_be_determined",
            ),
        },
        key="adenomyosis",
    ),

    conditional_radio_multiple(
        label="Uterine Serosal Involvement",
        options=[
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": text(
                label="Explain",
                key="uterine_serosal_involvement_cannot_be_determined",
            ),
        },
        key="uterine_serosal_involvement",
    ),

    conditional_radio_multiple(
        label="Lower Uterine Segment Involvement",
        options=[
            "Do not include",
            "Not identified",
            "Present, non-myoinvasive",
            "Present, myoinvasive",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": text(
                label="Explain",
                key=(
                    "lower_uterine_segment_involvement_"
                    "cannot_be_determined"
                ),
            ),
        },
        key="lower_uterine_segment_involvement",
    ),

    conditional_radio_multiple(
        label="Cervical Involvement",
        options=[
            (
                "Cannot be assessed "
                "(supracervical hysterectomy)"
            ),
            "Not identified",
            "Cervical stromal invasion",
            "Endocervical glandular involvement only",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cervical stromal invasion": (
                conditional_radio_multiple(
                    label="Percentage of Cervical Wall Involved",
                    options=[
                        "Specify percentage",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Specify percentage": text(
                            label="Specify Percentage",
                            suffix=" %",
                            key=(
                                "cervical_wall_involvement_"
                                "percentage"
                            ),
                        ),
                        "Cannot be determined": text(
                            label="Explain",
                            key=(
                                "cervical_wall_involvement_"
                                "cannot_be_determined"
                            ),
                        ),
                    },
                    child_value_options=[
                        "Specify percentage",
                    ],
                    key="percentage_cervical_wall_involved",
                )
            ),

            "Cannot be determined": text(
                label="Explain",
                key="cervical_involvement_cannot_be_determined",
            ),
        },
        key="cervical_involvement",
    ),

    checkbox_group(
        label="Other Tissue / Organ Involvement",
        options=[
            (
                "Not applicable "
                "(no other tissues / organs submitted)"
            ),
            (
                "Not identified "
                "(other tissues / organs submitted and not involved)"
            ),
            "Right ovary",
            "Left ovary",
            "Ovary (side not specified)",
            "Right fallopian tube",
            "Left fallopian tube",
            "Fallopian tube (side not specified)",
            "Vagina",
            "Right parametrium",
            "Left parametrium",
            "Parametrium (side not specified)",
            "Pelvic wall",
            "Bladder wall without mucosal involvement",
            "Bladder wall with mucosal involvement",
            "Bowel wall without mucosal involvement",
            "Bowel wall with mucosal involvement",
            "Other organs / tissue",
            "Cannot be determined",
        ],
        conditional_fields={
            "Other organs / tissue": text(
                label="Specify Other Organ or Tissue",
                key="other_tissue_organ_involvement_other",
            ),

            "Cannot be determined": text(
                label="Explain",
                key=(
                    "other_tissue_organ_involvement_"
                    "cannot_be_determined"
                ),
            ),
        },
        exclusive_options=[
            (
                "Not applicable "
                "(no other tissues / organs submitted)"
            ),
            (
                "Not identified "
                "(other tissues / organs submitted and not involved)"
            ),
            "Cannot be determined",
        ],
        key="other_tissue_organ_involvement",
    ),

    conditional_radio_multiple(
        label="Peritoneal / Pelvic Washings / Ascitic Fluid",
        options=[
            "Do not include",
            "Not submitted",
            "Negative for malignant cells",
            "Malignant cells present",
            "Atypical",
            "Suspicious for malignancy",
            "Results pending",
        ],
        conditional_fields={
            "Atypical": text(
                label="Explain",
                key="peritoneal_washings_atypical_explanation",
            ),

            "Suspicious for malignancy": text(
                label="Explain",
                key=(
                    "peritoneal_washings_"
                    "suspicious_for_malignancy_explanation"
                ),
            ),
        },
        key="peritoneal_pelvic_washings",
    ),

    conditional_radio_multiple(
        label="Lymphatic and / or Vascular Invasion",
        options=[
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Present": conditional_radio_multiple(
                label="Extent of Lymphatic and / or Vascular Invasion",
                options=[
                    "Less than or equal to 4 foci",
                    "Greater than or equal to 5 foci",
                ],
                conditional_fields={
                    "Less than or equal to 4 foci": text(
                        label="Specify Number of Foci",
                        key="lymphovascular_invasion_number_of_foci",
                    ),
                },
                key="lymphovascular_invasion_extent",
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

    ("section", "MARGINS"),

    conditional_radio_multiple(
        label="Margin Status",
        options=[
            "Not applicable",
            "All margins negative for carcinoma",
            "Carcinoma present at margin",
            "Cannot be determined",
        ],
        conditional_fields={
            "All margins negative for carcinoma": [
                uterine_margin_sites(
                    label="Closest Margin(s) to Carcinoma",
                    key="closest_margins_to_carcinoma",
                ),

                conditional_value(
                    label="Distance from Carcinoma to Closest Margin",
                    options=[
                        "Exact distance",
                        "At least",
                        "Less than",
                        "Less than 1 mm",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Exact distance": (
                            "Specify Exact Distance",
                            " mm",
                        ),
                        "At least": (
                            "Specify Minimum Distance",
                            " mm",
                        ),
                        "Less than": (
                            "Specify Distance",
                            " mm",
                        ),
                        "Cannot be determined": (
                            "Explain",
                            "",
                        ),
                    },
                    key="distance_to_closest_margin",
                ),
            ],

            "Carcinoma present at margin": uterine_margin_sites(
                label="Margin(s) Involved by Carcinoma",
                key="margins_involved_by_carcinoma",
            ),

            "Cannot be determined": text(
                label="Explain",
                key="margin_status_cannot_be_determined",
            ),
        },
        key="margin_status",
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
                checkbox_group(
                    label="Regional Lymph Node Findings",
                    options=[
                        (
                            "All regional lymph nodes "
                            "negative for tumor cells"
                        ),
                        "Tumor present in pelvic lymph node(s)",
                        (
                            "Tumor present in para-aortic "
                            "lymph node(s)"
                        ),
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        (
                            "Tumor present in pelvic "
                            "lymph node(s)"
                        ): pelvic_positive_node_fields(),

                        (
                            "Tumor present in para-aortic "
                            "lymph node(s)"
                        ): para_aortic_positive_node_fields(),

                        "Other": text(
                            label=(
                                "Specify Other Regional "
                                "Lymph Node Finding"
                            ),
                            key="regional_lymph_nodes_other",
                        ),

                        "Cannot be determined": text(
                            label="Explain",
                            key=(
                                "regional_lymph_nodes_"
                                "cannot_be_determined"
                            ),
                        ),
                    },
                    exclusive_options=[
                        (
                            "All regional lymph nodes "
                            "negative for tumor cells"
                        ),
                        "Cannot be determined",
                    ],
                    key="regional_lymph_node_findings",
                ),

                nodal_count_field(
                    label=(
                        "Total Number of Pelvic Nodes Examined "
                        "(sentinel and non-sentinel)"
                    ),
                    key="total_pelvic_nodes_examined",
                ),

                nodal_count_field(
                    label=(
                        "Number of Pelvic Sentinel Nodes Examined "
                        "(required only if applicable)"
                    ),
                    include_not_applicable=True,
                    key="pelvic_sentinel_nodes_examined",
                ),

                nodal_count_field(
                    label=(
                        "Total Number of Para-aortic Nodes Examined "
                        "(sentinel and non-sentinel)"
                    ),
                    key="total_para_aortic_nodes_examined",
                ),

                nodal_count_field(
                    label=(
                        "Number of Para-aortic Sentinel Nodes "
                        "Examined (required only if applicable)"
                    ),
                    include_not_applicable=True,
                    key="para_aortic_sentinel_nodes_examined",
                ),
            ],
        },
        key="regional_lymph_node_status",
    ),

    ("section", "DISTANT METASTASIS"),

    checkbox_group(
        label=(
            "Distant Site(s) Involved, if applicable "
            "(select all that apply)"
        ),
        options=[
            "Not applicable",
            "Omentum",
            "Extrapelvic peritoneum",
            "Inguinal lymph node(s)",
            "Lung",
            "Liver",
            "Bone",
            "Other",
            "Cannot be determined",
        ],
        conditional_fields={
            "Omentum": text(
                label="Specify Omental Involvement",
                key="distant_metastasis_omentum",
            ),

            "Extrapelvic peritoneum": text(
                label="Specify Extrapelvic Peritoneal Involvement",
                key="distant_metastasis_extrapelvic_peritoneum",
            ),

            "Inguinal lymph node(s)": text(
                label="Specify Inguinal Lymph Node Involvement",
                key="distant_metastasis_inguinal_lymph_nodes",
            ),

            "Lung": text(
                label="Specify Lung Involvement",
                key="distant_metastasis_lung",
            ),

            "Liver": text(
                label="Specify Liver Involvement",
                key="distant_metastasis_liver",
            ),

            "Bone": text(
                label="Specify Bone Involvement",
                key="distant_metastasis_bone",
            ),

            "Other": text(
                label="Specify Other Distant Site",
                key="distant_metastasis_other",
            ),

            "Cannot be determined": text(
                label="Explain",
                key="distant_metastasis_cannot_be_determined",
            ),
        },
        exclusive_options=[
            "Not applicable",
            "Cannot be determined",
        ],
        key="distant_sites_involved",
    ),

    ("section", "pTNM CLASSIFICATION (AJCC 8th Edition)"),

    option_toggle(
        label="Show pTNM definitions in table",
        key=UTERUS_TNM_DEFINITIONS_KEY,
        default=False,
    ),

    checkbox_group(
        label=(
            "Modified Classification "
            "(required only if applicable)"
        ),
        options=[
            "Not applicable",
            "y (post-neoadjuvant therapy)",
            "r (recurrence)",
        ],
        exclusive_options=[
            "Not applicable",
        ],
        key="uterus_modified_classification",
    ),

    radio_toggle(
        label="pT Category",
        options=UTERUS_PT_CATEGORY_OPTIONS,
        session_key=UTERUS_TNM_DEFINITIONS_KEY,
        key="uterus_pt_category",
    ),

    radio_toggle(
        label="T Suffix (required only if applicable)",
        options=UTERUS_T_SUFFIX_OPTIONS,
        session_key=UTERUS_TNM_DEFINITIONS_KEY,
        key="uterus_t_suffix",
    ),

    radio_toggle(
        label="pN Category",
        options=UTERUS_PN_CATEGORY_OPTIONS,
        session_key=UTERUS_TNM_DEFINITIONS_KEY,
        key="uterus_pn_category",
    ),

    radio_toggle(
        label="N Suffix (required only if applicable)",
        options=UTERUS_N_SUFFIX_OPTIONS,
        session_key=UTERUS_TNM_DEFINITIONS_KEY,
        key="uterus_n_suffix",
    ),

    radio_toggle(
        label=(
            "pM Category "
            "(required only if confirmed pathologically)"
        ),
        options=UTERUS_PM_CATEGORY_OPTIONS,
        session_key=UTERUS_TNM_DEFINITIONS_KEY,
        key="uterus_pm_category",
    ),

    ("section", "FIGO STAGE"),

    option_toggle(
        label="Show FIGO stage definitions in table",
        key=UTERUS_FIGO_DEFINITIONS_KEY,
        default=False,
    ),

    radio_toggle(
        label=(
            "FIGO Stage "
            "(FIGO 2009 Staging / 2018 FIGO Cancer Report) "
            "(Note N)"
        ),
        options=UTERUS_FIGO_2009_OPTIONS,
        session_key=UTERUS_FIGO_DEFINITIONS_KEY,
        key="uterus_figo_stage_2009",
    ),

    radio_toggle(
        label=(
            "FIGO Stage "
            "(2023 Staging for Cancer of the Endometrium) "
            "(Note N)"
        ),
        options=UTERUS_FIGO_2023_OPTIONS,
        session_key=UTERUS_FIGO_DEFINITIONS_KEY,
        key="uterus_figo_stage_2023",
    ),



    
]