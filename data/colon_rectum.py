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

DISPLAY_NAME = "Colon and Rectum, Resection"

SYNOPTIC = [
    ("title", "CASE SUMMARY", "(COLON AND RECTUM: Resection)\n Standard(s): AJCC 8 "),

    ("section", "SPECIMEN"),

    radio_other(
        "Procedure",
        [
            "Right hemicolectomy",
            "Transverse colectomy",
            "Left hemicolectomy",
            "Sigmoidectomy",
            "Low anterior resection",
            "Total abdominal colectomy",
            "Abdominoperineal resection",
        ],
    ),

    radio_other(
        "Macroscopic Evaluation of Mesorectum",
        [
            "Not applicable ",
            "Complete",
            "Near complete",
            "Incomplete",
        ],
    ),

    ("section", "TUMOR"),

    conditional_radio_multiple(
        label="Tumor Site",
        options=[
            "Cecum",
            "Ileocecal valve",
            "Ascending colon",
            "Hepatic flexure",
            "Transverse colon",
            "Splenic flexure",
            "Descending colon",
            "Sigmoid colon",
            "Rectosigmoid",
            "Rectum",
        ],
        conditional_fields={
            "Rectum": [
                radio(
                    "Rectal Location",
                    [
                        "Entirely above anterior peritoneal reflection",
                        "Entirely below anterior peritoneal reflection",
                        "Straddles anterior peritoneal reflection",
                        "Not specified",
                    ],
                )
            ]
        },
        allow_other=True,
    ),

    radio_other(
        "Histologic Type",
        [
            "Adenocarcinoma",
            "Mucinous adenocarcinoma",
            "Poorly cohesive carcinoma",
            "Signet-ring cell carcinoma",
            "Carcinoma with sarcomatoid component",
            "Large cell neuroendocrine carcinoma",
            "Small cell neuroendocrine carcinoma",
        ],
    ),

    radio_other(
        "Histologic Grade",
        [
            "Well-differentiated",
            "Moderately differentiated",
            "Poorly differentiated",
        ],
    ),

    conditional_value(
        label="Tumor Size",
        options=[
            "Exact size",
            "At least",
            "No evidence of invasive carcinoma following neoadjuvant therapy",
            "Not applicable ",
            "Cannot be determined",
        ],
        value_fields={
            "Exact size": ("Size", " cm"),
            "At least": ("Size", " cm"),
            "Cannot be determined": ("Comment", ""),
        },
    ),

    conditional_value(
        label="Multiple Primary Sites",
        options=[
            "Not applicable ",
            "Present",
        ],
        value_fields={
            "Present": (
                "Specify additional primary site(s)",
                "",
            ),
        },
    ),

    conditional_radio_multiple(
        label="Tumor Extent",
        options=[
            "No invasion (high-grade dysplasia)",
            "Invades lamina propria / muscularis mucosae (intramucosal carcinoma)",
            "Invades submucosa",
            "Invades into muscularis propria",
            "Invades through muscularis propria into the pericolic or perirectal tissue",
            "Invades visceral peritoneum (including tumor continuous with serosal surface through area of inflammation)",
            "Directly invades or adheres to adjacent structure(s)",
            "Cannot be determined",
        ],
        conditional_fields={
            "Directly invades or adheres to adjacent structure(s)": [
                text("Specify adjacent structure(s)")
            ],
            "Cannot be determined": [
                text("Comment", key="tumor_extent_comment",)
            ],
        },
    ),

    conditional_radio_multiple(
        label="Submucosal Invasion",
        options=[
            "Not applicable (not a pT1 tumor)",
            "Not identified",
            "Present",
        ],
        conditional_fields={
            "Present": [
                conditional_radio_multiple(
                    label="Depth of Submucosal Invasion",
                    options=[
                        "Less than 1 mm",
                        "Greater than or equal to 1 mm and less than 2 mm",
                        "Greater than 2 mm",
                        "Exact depth in Millimeters (mm)",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Exact depth in Millimeters (mm)": [
                            text("Exact depth")
                        ],
                        "Cannot be determined": [
                            text("Comment", key="depth_of_submucosal_invasion_comment",)
                        ],
                    },
                ),
                conditional_radio_multiple(
                    label="Extent of Submucosal Invasion",
                    options=[
                        "Tumor invades into upper one third of submucosa",
                        "Tumor invades into middle one third of submucosa",
                        "Tumor invades into lower one third of submucosa",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Cannot be determined": [
                            text("Comment", key="extent_of_submucosal_invasion_comment",)
                        ],
                    },
                ),
            ]
        },
    ),

    conditional_radio_multiple(
        label="Macroscopic Tumor Perforation",
        options=[
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text("Comment", key="tumor_perforation_comment",),
            ],
        },
    ),

    checkbox_group(
        label="Lymphatic and / or Vascular Invasion",
        options=[
            "Not identified",
            "Small vessel",
            "Large vessel (venous), intramural",
            "Large vessel (venous), extramural",
            "Present, NOS",
            "Cannot be determined",
        ],
        default="Not identified",
        exclusive_options=["Not identified"],
        conditional_fields={
            "Cannot be determined": text("Comment", key="LVI_comment",),
        },
    ),

    conditional_radio_multiple(
        label="Perineural Invasion",
        options=[
            "Not identified",
            "Present",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    "Comment",
                    key="perineural_invasion_comment",
                ),
            ],
        },
    ),

    conditional_radio_multiple(
        label="Tumor Budding Score",
        options=[
            "Do not include",
            "Not applicable ",
            "Low (0-4)",
            "Intermediate (5-9)",
            "High (10 or more)",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    "Comment",
                    key="tumor_budding_comment",
                ),
            ],
        },
    ),

    conditional_radio_multiple(
        label="Treatment Effect",
        options=[
            "No known presurgical therapy",
            "Present, with no viable cancer cells (complete response, score 0)",
            "Present, with single cells or rare small groups of cancer cells (near complete response, score 1)",
            "Present, with residual cancer showing evident tumor regression, but more than single cells or rare small groups of cancer cells (partial response, score 2)",
            "Present, NOS",
            "Absent, with extensive residual cancer and no evident tumor regression (poor or no response, score 3)",
            "Cannot be determined",
        ],
        conditional_fields={
            "Cannot be determined": [
                text(
                    "Comment",
                    key="treatment_effect_comment",
                ),
            ],
        },
    ),

    ("section", "MARGINS"),

    conditional_radio_multiple(
        label="Margin Status for Invasive Carcinoma",
        options=[
            "All margins negative for invasive carcinoma",
            "Invasive carcinoma present at margin",
            "Other",
            "Cannot be determined",
            "Not applicable ",
        ],
        conditional_fields={
            "All margins negative for invasive carcinoma": [
                checkbox_group(
                    label="Closest Margin(s) to Invasive Carcinoma",
                    options=[
                        "Proximal",
                        "Distal",
                        "Radial (circumferential)",
                        "Mesenteric",
                        "Deep",
                        "Mucosal",
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other": [
                            text(
                                "Comment",
                                key="closest_margin_other",
                            ),
                        ],
                        "Cannot be determined": [
                            text(
                                "Comment",
                                key="closest_margin_comment",
                            ),
                        ],
                    },
                ),

                conditional_value(
                    label="Distance from Invasive Carcinoma to Closest Margin",
                    options=[
                        "Do not include",
                        "Not applicable",
                        "Exact distance in cm",
                        "Greater than 1 cm",
                        "Exact distance in mm",
                        "Greater than 10 mm",
                        "Other",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Exact distance in cm": ("Distance", " cm"),
                        "Exact distance in mm": ("Distance", " mm"),
                        "Other": ("Comment", ""),
                        "Cannot be determined": ("Comment", ""),
                    },
                ),

                conditional_value(
                    label="Distance from Invasive Carcinoma to Proximal Margin",
                    options=[
                        "Do not include",
                        "Not applicable",
                        "Distance already reported as closest margin",
                        "Exact distance in cm",
                        "Greater than 1 cm",
                        "Exact distance in mm",
                        "Greater than 10 mm",
                        "Other",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Distance already reported as closest margin": (
                            "Comment",
                            "",
                        ),
                        "Exact distance in cm": ("Distance", " cm"),
                        "Exact distance in mm": ("Distance", " mm"),
                        "Other": ("Comment", ""),
                        "Cannot be determined": ("Comment", ""),
                    },
                ),

                conditional_value(
                    label="Distance from Invasive Carcinoma to Radial (Circumferential) Margin",
                    options=[
                        "Do not include",
                        "Not applicable",
                        "Distance already reported as closest margin",
                        "Exact distance in cm",
                        "Greater than 1 cm",
                        "Exact distance in mm",
                        "Greater than 10 mm",
                        "Other",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Distance already reported as closest margin": (
                            "Comment",
                            "",
                        ),
                        "Exact distance in cm": ("Distance", " cm"),
                        "Exact distance in mm": ("Distance", " mm"),
                        "Other": ("Comment", ""),
                        "Cannot be determined": ("Comment", ""),
                    },
                ),

                conditional_value(
                    label="Distance from Invasive Carcinoma to Distal Margin",
                    options=[
                        "Do not include",
                        "Not applicable",
                        "Distance already reported as closest margin",
                        "Exact distance in cm",
                        "Greater than 1 cm",
                        "Exact distance in mm",
                        "Greater than 10 mm",
                        "Other",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Distance already reported as closest margin": (
                            "Comment",
                            "",
                        ),
                        "Exact distance in cm": ("Distance", " cm"),
                        "Exact distance in mm": ("Distance", " mm"),
                        "Other": ("Comment", ""),
                        "Cannot be determined": ("Comment", ""),
                    },
                ),
            ],

            "Invasive carcinoma present at margin": [
                checkbox_group(
                    label="Margin(s) Involved by Invasive Carcinoma",
                    options=[
                        "Proximal",
                        "Distal",
                        "Radial (circumferential)",
                        "Mesenteric",
                        "Deep",
                        "Mucosal",
                        "Other",
                        "Cannot be determined",
                    ],
                    conditional_fields={
                        "Other": [
                            text(
                                "Comment",
                                key="closest_margin_other",
                            ),
                        ],
                        "Cannot be determined": [
                            text(
                                "Comment",
                                key="closest_margin_comment",
                            ),
                        ],
                    },
                ),
            ],

            "Other": [
                text(
                    "Comment",
                    key="invasive_margin_status_other",
                ),
            ],

            "Cannot be determined": [
                text(
                    "Comment",
                    key="invasive_margin_status_cannot_determine",
                ),
            ],
        },
    ),

checkbox_group(
    label="Margin Status for Non-Invasive Tumor",
    options=[
        "All margins negative for high-grade dysplasia / intramucosal carcinoma and low-grade dysplasia",
        "High-grade dysplasia / intramucosal carcinoma present at margin",
        "Low-grade dysplasia present at margin",
        "Other",
        "Cannot be determined",
    ],
    default="All margins negative for high-grade dysplasia / intramucosal carcinoma and low-grade dysplasia",
    exclusive_options=["All margins negative for high-grade dysplasia / intramucosal carcinoma and low-grade dysplasia"],
    conditional_fields={
        "High-grade dysplasia / intramucosal carcinoma present at margin":
            checkbox_group(
                label="Margin(s) Involved by High-Grade Dysplasia / Intramucosal Carcinoma",
                options=[
                    "Proximal",
                    "Distal",
                    "Mucosal",
                    "Other",
                    "Cannot be determined",
                ],
            ),

        "Low-grade dysplasia present at margin":
            checkbox_group(
                label="Margin(s) Involved by Low-Grade Dysplasia",
                options=[
                    "Proximal",
                    "Distal",
                    "Mucosal",
                    "Other",
                    "Cannot be determined",
                ],
            ),

        "Other": text(
            "Comment",
            key="noninvasive_margin_status_other",
        ),

        "Cannot be determined": text(
            "Comment",
            key="noninvasive_margin_status_cannot_determine",
        ),
    },
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
            "Tumor present in regional lymph node(s)": [
                conditional_value(
                    label="Number of Lymph Nodes with Tumor",
                    options=[
                        "Not applicable",
                        "Exact number",
                        "At least",
                        "Other",
                        "Cannot be determined",
                    ],
                    value_fields={
                        "Exact number": ("Number", ""),
                        "At least": ("Number", ""),
                        "Other": ("Comment", ""),
                        "Cannot be determined": ("Comment", ""),
                    },
                ),
            ],
        },
    ),

        conditional_value(
            label="Number of Lymph Nodes Examined",
            options=[
                "Not applicable",
                "Exact number",
                "At least",
                "Other",
                "Cannot be determined",
            ],
            value_fields={
                "Exact number": ("Number", ""),
                "At least": ("Number", ""),
                "Other": ("Comment", ""),
                "Cannot be determined": ("Comment", ""),
            },
        ),

    ("section", "DISTANT METASTASIS"),

    checkbox_group(
        label="Distant Site(s) Involved",
        options=[
            "Not applicable ",
            "Non-regional lymph node(s)",
            "Liver",
            "Other",
            "Cannot be determined",
        ],
        default="Not applicable ",
        exclusive_options=["Not applicable "],

        conditional_fields={
            "Non-regional lymph node(s)": text(
                "Comment",
                key="distant_site_nonregional_nodes_comment",
            ),
            "Liver": text(
                "Comment",
                key="distant_site_liver_comment",
            ),
            "Other": text(
                "Comment",
                key="distant_site_other_comment",
            ),
            "Cannot be determined": text(
                "Comment",
                key="distant_site_cannot_determine_comment",
            ),
        },
    ),

    checkbox_group(
        label="Additional Findings",
        options=[
            "Do not include",
            "None identified",
            "Adenoma(s)",
            "Ulcerative colitis",
            "Crohn disease",
            "Diverticulosis",
            "Dysplasia arising in inflammatory bowel disease",
            "Other",
        ],
        exclusive_options=["Do not include", "None identified"],
        conditional_fields={
            "Other": text(
                "Comment",
                key="additional_findings_other",
            ),
        },
        default="Do not include",
    ),

    ("section", "SPECIAL STUDIES"),

    conditional_value(
        label="MMR Protein Immunohistochemistry",
        options=[
            "Not applicable",
            "Performed on patient's prior biopsy showing no loss of nuclear expression of MMR proteins, indicating low probability of MSI-H",
            "Immunostains for MLH1, PMS2, MSH2, and MSH6 shows no loss of nuclear expression of MMR proteins, indicating low probability of MSI-H",
            """Immunostains for MLH1, PMS2, MSH2, and MSH6 shows loss of nuclear expression of MLH1 and PMS2: 
            testing for methylation of the MLH1 promoter and / or mutation of BRAF is indicated (the presence 
            of a BRAF V600E mutation and / or MLH1 methylation suggests that the tumor is sporadic and germline 
            evaluation is probably not indicated; absence of both MLH1 methylation and of BRAF V600E mutation 
            suggests the possibility of Lynch Syndrome and sequencing and / or large deletion / duplication testing 
            of germline MLH1 may be indicated)""",
            """Immunostains for MLH1, PMS2, MSH2, and MSH6 shows loss of nuclear expression of MLH1 and PMS2: 
            testing for methylation of the MLH1 promoter is being performed, result to follow in an addendum""",
            """Testing on prior biopsy showed loss of nuclear expression of MLH1 and PMS2 with MLH1 promotor 
            hypermethylation suggesting that the tumor is sporadic and germline 
            evaluation is probably not indicated""",
            """Testing on prior biopsy showed loss of nuclear expression of MLH1 and PMS2 with absent MLH1 promotor 
            hypermethylation suggesting the possibility of Lynch Syndrome and sequencing and / or large deletion / duplication testing 
            of germline MLH1 may be indicated)""",
            """Loss of nuclear expression of MSH2 and MSH6: high probability of Lynch syndrome
            (sequencing and / or large deletion / duplication testing of germline MSH2 may be indicated and, if
            negative, sequencing and / or large deletion / duplication testing of germline MSH6 may be
            indicated) """,
            """Loss of nuclear expression of MSH6 only: high probability of Lynch syndrome (sequencing and /
            or large deletion / duplication testing of germline MSH6 may be indicated)""",
            """ Loss of nuclear expression of PMS2 only: high probability of Lynch syndrome (sequencing and /
            or large deletion / duplication testing of germline PMS2 may be indicated)""",
            "Other",
            "Cannot be determined",
        ],
        value_fields={
            "Other": ("Comment", ""),
            "Cannot be determined": ("Comment", ""),
        },
    ),

    ("section", "pTNM CLASSIFICATION (AJCC 8th Edition)"),

    option_toggle(
        label="Include full TNM definitions in table",
        key="show_full_tnm",
        default=False,
    ),

    checkbox_group(
        label="Modified Classification",
        options=[
            "Do not include",
            "Not applicable ",
            "y (post-neoadjuvant therapy)",
            "r (recurrence)",
        ],
        default="Do not include",
        exclusive_options=["Do not include", "Not applicable "],
    ),

    radio_toggle(
        label="pT Category",
        session_key="show_full_tnm",
        options=[
            (
                "pT not assigned: Cannot be determined based on available pathological information",
                "pT not assigned",
            ),
            (
                "pT0: No evidence of primary tumor",
                "pT0",
            ),
            (
                "pTis: Carcinoma in situ, intramucosal carcinoma involving the lamina propria without extension through the muscularis mucosae",
                "pTis",
            ),
            (
                "pT1: Tumor invades the submucosa through the muscularis mucosae but not into the muscularis propria",
                "pT1",
            ),
            (
                "pT2: Tumor invades the muscularis propria",
                "pT2",
            ),
            (
                "pT3: Tumor invades through the muscularis propria into pericolorectal tissues",
                "pT3",
            ),
            (
                "pT4a: Tumor invades through the visceral peritoneum",
                "pT4a",
            ),
            (
                "pT4b: Tumor directly invades or adheres to adjacent organs or structures",
                "pT4b",
            ),
            (
                "pT4: Subcategory cannot be determined",
                "pT4",
            ),
        ],
    ),

    radio(
        "T Suffix",
        [
            "Do not include",
            "Not applicable",
            "(m) Multiple primary synchronous tumors in a single organ",
        ],
    ),

    radio_toggle(
        label="pN Category",
        session_key="show_full_tnm",
        options=[
            (
                "pN not assigned: No nodes submitted or found",
                "pN not assigned",
            ),
            (
                "pN not assigned: Cannot be determined based on available pathological information",
                "pN not assigned",
            ),
            (
                "pN0: No regional lymph node metastasis",
                "pN0",
            ),
            (
                "pN1a: One regional lymph node is positive",
                "pN1a",
            ),
            (
                "pN1b: Two or three regional lymph nodes are positive",
                "pN1b",
            ),
            (
                "pN1c: No regional lymph nodes are positive, but tumor deposits are present",
                "pN1c",
            ),
            (
                "pN1: Subcategory cannot be determined",
                "pN1",
            ),
            (
                "pN2a: Four to six regional lymph nodes are positive",
                "pN2a",
            ),
            (
                "pN2b: Seven or more regional lymph nodes are positive",
                "pN2b",
            ),
            (
                "pN2: Subcategory cannot be assessed",
                "pN2",
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
                "Not applicable",
            ),
            (
                "pM1a: Metastasis to one site or organ without peritoneal metastasis",
                "pM1a",
            ),
            (
                "pM1b: Metastasis to two or more sites or organs without peritoneal metastasis",
                "pM1b",
            ),
            (
                "pM1c: Metastasis to the peritoneal surface, alone or with other distant metastases",
                "pM1c",
            ),
            (
                "pM1: Subcategory cannot be determined",
                "pM1",
            ),
        ],
    ),

]

