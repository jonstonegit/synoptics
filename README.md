Purpose:
    Build pathology CAP synoptic reports.

Users:
    Pathologists and trascriptionists

Goals:
    - Display CAP protocols
    - Fill out reports quickly
    - Validate required fields
    - Export text and add cleaning to LigoLab and EPIC LISs
    - Save JSON

Current architecture:
    - app.py runs the program
    - synoptic_engine folder contains files that build the table
    - data folder contains site specific files used to build each synoptic
    - images folder contains image to display on splash screen

app.py
    Streamlit UI

Future work
    Complete synoptics from more sites
    Work on formatting optimization and customization
