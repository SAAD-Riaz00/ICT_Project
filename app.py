# ============================================================
# MECHANICAL ENGINEERING TOOLKIT
# Developed By: Saad Riaz
# Roll Number: 25-ME-47
# Department: Mechanical Engineering
# ============================================================

import streamlit as st
import math
import pandas as pd

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Mechanical Engineering Toolkit",
    page_icon="⚙️",
    layout="wide"
)

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1537462715879-360eeb61a0ad");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"]::before{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(5,5,5,0.84);
    z-index: -1;
}

.main-title{
    text-align:center;
    font-size:42px;
    color:white;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:#d0d0d0;
}

.section-card{
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0px 0px 12px rgba(0,0,0,0.5);
}

.metric-box{
    background: rgba(255,255,255,0.08);
    padding:15px;
    border-radius:15px;
    text-align:center;
    margin-bottom:15px;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

st.markdown("""
<div class="main-title">
⚙️ Mechanical Engineering Department Toolkit
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Mechanical Unit Converter • Engineering Utilities • Attendance Manager • Timetable System
<br><br>
<b>Developed By:</b> Saad Riaz |
<b>Roll Number:</b> 25-ME-47 |
<b>Department:</b> Mechanical Engineering
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# DATABASES
# ============================================================

# ------------------------------------------------------------
# UNIT CONVERSION DATABASE
# ------------------------------------------------------------

UNIT_CATEGORIES = {

    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048
    },

    "Mass": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ton": 1000
    },

    "Force": {
        "Newton": 1,
        "Kilonewton": 1000,
        "Pound-force": 4.44822
    },

    "Pressure": {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100000,
        "PSI": 6894.76
    },

    "Speed": {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704
    }
}

# ------------------------------------------------------------
# MATERIAL DENSITY DATABASE
# ------------------------------------------------------------

MATERIAL_DENSITY = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Titanium": 4500,
    "Brass": 8500,
    "Concrete": 2400,
    "Rubber": 1520,
    "Wood": 700,
    "Glass": 2500,
    "Gold": 19300,
    "Silver": 10490
}

# ------------------------------------------------------------
# SCIENTIFIC CONSTANTS
# ------------------------------------------------------------

SCIENTIFIC_CONSTANTS = {
    "Gravity": "9.81 m/s²",
    "Speed of Light": "3 × 10⁸ m/s",
    "Gas Constant": "8.314 J/mol·K",
    "Atmospheric Pressure": "101325 Pa",
    "Planck Constant": "6.626 × 10⁻³⁴ Js"
}

# ------------------------------------------------------------
# ATTENDANCE SUBJECTS
# ------------------------------------------------------------

SUBJECTS = [
    "ICT",
    "CAD Lab",
    "EMATE",
    "EE",
    "EM-I",
    "THERMO-I",
    "LADE",
    "ICT Lab"
]

# ------------------------------------------------------------
# TIMETABLE DATABASE
# ------------------------------------------------------------

TIMETABLES = {

    "2025 / A": [
        ["1-3", "TH-I"],
        ["4-6", "CAD (A)"],
        ["1-3", "LA&DE"],
        ["4-5", "MATE"],
        ["1-2", "EE"],
        ["4-5", "ICT"],
        ["1-3", "EM-I"],
        ["4-6", "ICT (A)"],
        ["3-4", "ICP"]
    ],

    "2025 / B": [
        ["1-2", "MATE"],
        ["4-6", "TH-I"],
        ["1-3", "CAD (B)"],
        ["4-6", "EM-I"],
        ["1-2", "ICT"],
        ["3-4", "EE"],
        ["7-9", "ICT (B)"],
        ["1-3", "LA&DE"],
        ["3-4", "ICP"]
    ],

    "2025 / C": [
        ["1-2", "ICT"],
        ["7-9", "CAD (C)"],
        ["1-2", "MATE"],
        ["3-4", "EE"],
        ["7-9", "EM-I"],
        ["1-3", "TH-I"],
        ["5-7", "LA&DE"],
        ["1-3", "ICT (C)"],
        ["1-2", "ICP"]
    ],

    "2025 / D": [
        ["1-2", "ICT"],
        ["4-5", "MATE"],
        ["1-2", "EE"],
        ["4-6", "CAD (D)"],
        ["1-3", "LA&DE"],
        ["4-6", "ICT (D)"],
        ["1-3", "TH-I"],
        ["5-7", "EM-I"],
        ["1-2", "ICP"]
    ]
}

# ============================================================
# FUNCTIONS
# ============================================================

def convert_units(category, value, from_unit, to_unit):

    try:

        units = UNIT_CATEGORIES[category]

        base = value * units[from_unit]

        result = base / units[to_unit]

        return result

    except:
        return None

def scientific_calculator(expression):

    allowed = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "log10": math.log10,
        "pi": math.pi,
        "e": math.e,
        "pow": pow
    }

    return eval(expression, {"__builtins__": {}}, allowed)

# ============================================================
# MAIN SECTIONS
# ============================================================

main_tab1, main_tab2 = st.tabs([
    "⚙️ Engineering Utilities",
    "🎓 Student Portal"
])

# ============================================================
# ENGINEERING UTILITIES SECTION
# ============================================================

with main_tab1:

    util1, util2, util3, util4 = st.tabs([
        "🔄 Unit Converter",
        "🧱 Material Density",
        "📘 Constants",
        "🧮 Calculator"
    ])

    # --------------------------------------------------------
    # UNIT CONVERTER
    # --------------------------------------------------------

    with util1:

        st.markdown('<div class="section-card">', unsafe_allow_html=True)

        st.subheader("Mechanical Unit Converter")

        category = st.selectbox(
            "Select Category",
            list(UNIT_CATEGORIES.keys())
        )

        units = list(UNIT_CATEGORIES[category].keys())

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox("From Unit", units)

        with col2:
            to_unit = st.selectbox("To Unit", units)

        value = st.number_input(
            "Enter Value",
            value=0.0
        )

        if st.button("Convert"):

            result = convert_units(
                category,
                value,
                from_unit,
                to_unit
            )

            if result is not None:

                st.success(
                    f"{value} {from_unit} = {result:.5f} {to_unit}"
                )

            else:
                st.error("Conversion Error")

        st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # MATERIAL DENSITY
    # --------------------------------------------------------

    with util2:

        st.markdown('<div class="section-card">', unsafe_allow_html=True)

        st.subheader("Material Density Checker")

        search = st.text_input("Search Material")

        materials = []

        for material in MATERIAL_DENSITY:

            if search.lower() in material.lower():
                materials.append(material)

        if materials:

            selected = st.selectbox(
                "Select Material",
                materials
            )

            st.metric(
                "Density",
                f"{MATERIAL_DENSITY[selected]} kg/m³"
            )

        else:
            st.warning("No Material Found")

        st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # SCIENTIFIC CONSTANTS
    # --------------------------------------------------------

    with util3:

        st.subheader("Engineering Scientific Constants")

        cols = st.columns(2)

        index = 0

        for key, value in SCIENTIFIC_CONSTANTS.items():

            with cols[index % 2]:

                st.markdown(f"""
                <div class="metric-box">
                <h4>{key}</h4>
                <p>{value}</p>
                </div>
                """, unsafe_allow_html=True)

            index += 1

    # --------------------------------------------------------
    # SCIENTIFIC CALCULATOR
    # --------------------------------------------------------

    with util4:

        st.markdown('<div class="section-card">', unsafe_allow_html=True)

        st.subheader("Scientific Calculator")

        st.code("sqrt(25)")
        st.code("sin(pi/2)")
        st.code("pow(5,2)")

        expression = st.text_input(
            "Enter Expression"
        )

        if st.button("Calculate"):

            try:

                result = scientific_calculator(expression)

                st.success(f"Result = {result}")

            except:

                st.error("Invalid Expression")

        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# STUDENT PORTAL SECTION
# ============================================================

with main_tab2:

    student1, student2 = st.tabs([
        "📊 Attendance Manager",
        "📅 Class Timetable"
    ])

    # --------------------------------------------------------
    # ATTENDANCE MANAGER
    # --------------------------------------------------------

    with student1:

        st.subheader("Second Semester Attendance")

        for subject in SUBJECTS:

            st.markdown('<div class="section-card">', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:

                attended = st.number_input(
                    f"{subject} - Classes Attended",
                    min_value=0,
                    value=0,
                    key=subject + "attended"
                )

            with col2:

                total = st.number_input(
                    f"{subject} - Total Classes",
                    min_value=1,
                    value=1,
                    key=subject + "total"
                )

            percentage = (attended / total) * 100

            st.progress(min(int(percentage), 100))

            st.metric(
                "Attendance Percentage",
                f"{percentage:.2f}%"
            )

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("")

    # --------------------------------------------------------
    # TIMETABLE
    # --------------------------------------------------------

    with student2:

        st.subheader("Class Timetable")

        selected_class = st.selectbox(
            "Select Class",
            list(TIMETABLES.keys())
        )

        timetable_data = TIMETABLES[selected_class]

        df = pd.DataFrame(
            timetable_data,
            columns=["Time Slot", "Subject"]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.info("""
Class Timings:

1 → 08:30 am to 09:20 am  
2 → 09:20 am to 10:10 am  
3 → 10:10 am to 11:00 am  
4 → 11:00 am to 11:50 am  
5 → 11:50 am to 12:40 pm  
6 → 12:40 pm to 01:30 pm  
7 → 01:30 pm to 02:20 pm  
8 → 02:20 pm to 03:10 pm  
9 → 03:10 pm to 04:00 pm
""")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:white'>
⚙️ Mechanical Engineering Department Digital Toolkit
</div>
""", unsafe_allow_html=True)
