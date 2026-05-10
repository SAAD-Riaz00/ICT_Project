# app.py

# ============================================================
# Mechanical Unit Converter and Material Density Checker
# Developed By: Saad Riaz
# Roll Number: 25-ME-47
# ============================================================

# ---------------- STREAMLIT CLOUD DEPLOYMENT GUIDE ----------------
#
# STEP 1: Create a GitHub Repository
# ----------------------------------
# 1. Create a GitHub account if you do not already have one.
# 2. Click "New Repository"
# 3. Repository name example:
#       mechanical-unit-converter
# 4. Upload:
#       - app.py
#       - requirements.txt
#
# STEP 2: Push Files Using Git (Optional)
# ---------------------------------------
# Commands:
#
# git init
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git remote add origin YOUR_GITHUB_REPO_LINK
# git push -u origin main
#
# STEP 3: Deploy on Streamlit Cloud
# ---------------------------------
# 1. Go to:
#       https://streamlit.io/cloud
# 2. Login using GitHub
# 3. Click "New App"
# 4. Select your repository
# 5. Select:
#       app.py
# 6. Click "Deploy"
#
# STEP 4: Automatic Redeployment
# ------------------------------
# Every time you push new commits to GitHub,
# Streamlit Cloud automatically redeploys the app.
#
# STEP 5: Secrets / Environment Variables
# ---------------------------------------
# This project does NOT require secrets or API keys.
#
# ============================================================

import streamlit as st

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="wide"
)

# ------------------------------------------------------------
# HEADER SECTION
# ------------------------------------------------------------
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

st.markdown("""
### Developed By: **Saad Riaz**  
### Roll Number: **25-ME-47**
""")

st.markdown("---")

# ------------------------------------------------------------
# UNIT DEFINITIONS
# Conversion factors are relative to base SI units
# ------------------------------------------------------------

UNIT_CATEGORIES = {

    "Length": {
        "Meter (m)": 1,
        "Kilometer (km)": 1000,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048
    },

    "Mass": {
        "Kilogram (kg)": 1,
        "Gram (g)": 0.001,
        "Milligram (mg)": 0.000001,
        "Pound (lb)": 0.453592,
        "Ton (t)": 1000
    },

    "Force": {
        "Newton (N)": 1,
        "Kilonewton (kN)": 1000,
        "Pound-force (lbf)": 4.44822
    },

    "Pressure": {
        "Pascal (Pa)": 1,
        "Kilopascal (kPa)": 1000,
        "Bar": 100000,
        "PSI": 6894.76
    },

    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

# ------------------------------------------------------------
# MATERIAL DENSITY DATABASE
# Values are in kg/m³
# ------------------------------------------------------------

MATERIAL_DENSITY = {
    "Aluminum": 2700,
    "Steel": 7850,
    "Cast Iron": 7200,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Lead": 11340,
    "Concrete": 2400,
    "Wood": 700,
    "Glass": 2500,
    "Rubber": 1520,
    "Plastic (PVC)": 1380,
    "Water": 1000,
    "Ice": 917,
    "Gold": 19300,
    "Silver": 10490
}

# ------------------------------------------------------------
# TEMPERATURE CONVERSION FUNCTION
# ------------------------------------------------------------

def convert_temperature(value, from_unit, to_unit):
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin.
    """

    # Convert input to Celsius first
    if from_unit == "Celsius":
        celsius = value

    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "Kelvin":
        celsius = value - 273.15

    else:
        return None

    # Convert Celsius to target unit
    if to_unit == "Celsius":
        return celsius

    elif to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32

    elif to_unit == "Kelvin":
        return celsius + 273.15

    return None

# ------------------------------------------------------------
# GENERAL UNIT CONVERSION FUNCTION
# ------------------------------------------------------------

def convert_units(category, value, from_unit, to_unit):
    """
    Converts units using SI base conversion.
    """

    try:
        # Handle temperature separately
        if category == "Temperature":
            return convert_temperature(value, from_unit, to_unit)

        units = UNIT_CATEGORIES[category]

        # Convert to SI base unit
        base_value = value * units[from_unit]

        # Convert SI base unit to target unit
        converted_value = base_value / units[to_unit]

        return converted_value

    except Exception:
        return None

# ------------------------------------------------------------
# TABS FOR APPLICATION
# ------------------------------------------------------------

tab1, tab2 = st.tabs([
    "🔄 Unit Converter",
    "🧱 Material Density Checker"
])

# ============================================================
# UNIT CONVERTER TAB
# ============================================================

with tab1:

    st.subheader("Mechanical Unit Converter")

    # Category selection
    category = st.selectbox(
        "Select Unit Category",
        list(UNIT_CATEGORIES.keys())
    )

    units_list = list(UNIT_CATEGORIES[category].keys())

    # Layout columns
    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From Unit", units_list)

    with col2:
        to_unit = st.selectbox("To Unit", units_list)

    # User input
    value = st.number_input(
        "Enter Value",
        value=0.0,
        step=1.0,
        format="%.4f"
    )

    # Convert button
    if st.button("Convert"):

        try:
            result = convert_units(
                category,
                value,
                from_unit,
                to_unit
            )

            if result is not None:

                st.success(
                    f"{value} {from_unit} = {result:.4f} {to_unit}"
                )

            else:
                st.error("Conversion failed. Please check inputs.")

        except Exception:
            st.error("Invalid input detected.")

# ============================================================
# MATERIAL DENSITY CHECKER TAB
# ============================================================

with tab2:

    st.subheader("Material Density Checker")

    # Search box
    search_term = st.text_input(
        "Search Material",
        placeholder="Type material name..."
    )

    # Filter materials
    filtered_materials = []

    for material in MATERIAL_DENSITY.keys():
        if search_term.lower() in material.lower():
            filtered_materials.append(material)

    # If search result exists
    if filtered_materials:

        selected_material = st.selectbox(
            "Select Material",
            filtered_materials
        )

        density = MATERIAL_DENSITY[selected_material]

        st.info(
            f"Density of {selected_material}: "
            f"{density} kg/m³"
        )

    else:
        st.warning("No material found.")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")
st.caption("Mechanical Engineering Mini Project using Streamlit and Python")
