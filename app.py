# ------------------------------------------------------------
# PROFESSIONAL MECHANICAL ENGINEERING UI
# ------------------------------------------------------------

st.markdown("""
<style>

/* --------------------------------------------------
MAIN APP BACKGROUND
-------------------------------------------------- */

.stApp {

    background:
    linear-gradient(
        rgba(10,15,20,0.96),
        rgba(10,15,20,0.96)
    ),

    url("https://images.unsplash.com/photo-1509395176047-4a66953fd231?q=80&w=1920");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* --------------------------------------------------
MAIN CONTENT AREA
-------------------------------------------------- */

.block-container {

    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1350px;
}

/* --------------------------------------------------
HEADINGS
-------------------------------------------------- */

.main-title {

    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

.sub-title {

    text-align: center;
    color: #c8d2dc;
    font-size: 18px;
    line-height: 1.8;
    margin-bottom: 35px;
}

/* --------------------------------------------------
CARDS
-------------------------------------------------- */

.section-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 28px;

    margin-top: 18px;

    margin-bottom: 18px;

    box-shadow: 0px 6px 20px rgba(0,0,0,0.35);
}

/* --------------------------------------------------
METRIC BOX
-------------------------------------------------- */

.metric-box {

    background: rgba(255,255,255,0.04);

    border-radius: 18px;

    padding: 18px;

    border: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 18px;
}

/* --------------------------------------------------
TEXT COLORS
-------------------------------------------------- */

h1, h2, h3, h4, h5, h6, p, label {

    color: white !important;
}

/* --------------------------------------------------
INPUT FIELDS
-------------------------------------------------- */

.stTextInput input,
.stNumberInput input {

    background-color: rgba(255,255,255,0.05) !important;

    color: white !important;

    border-radius: 12px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* --------------------------------------------------
SELECT BOXES
-------------------------------------------------- */

.stSelectbox div[data-baseweb="select"] {

    background-color: rgba(255,255,255,0.05);

    border-radius: 12px;

    border: 1px solid rgba(255,255,255,0.08);
}

/* --------------------------------------------------
BUTTONS
-------------------------------------------------- */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    height: 50px;

    border: none;

    font-size: 16px;

    font-weight: 600;

    color: white;

    background: linear-gradient(
        135deg,
        #134e5e,
        #71b280
    );

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.02);

    background: linear-gradient(
        135deg,
        #1d6578,
        #85d69a
    );
}

/* --------------------------------------------------
TABS
-------------------------------------------------- */

.stTabs [role="tablist"] {

    gap: 10px;
}

.stTabs [role="tab"] {

    background: rgba(255,255,255,0.05);

    border-radius: 12px;

    padding: 10px 20px;

    color: white;

    font-weight: 600;
}

.stTabs [aria-selected="true"] {

    background: linear-gradient(
        135deg,
        #232526,
        #414345
    ) !important;
}

/* --------------------------------------------------
DATAFRAME
-------------------------------------------------- */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.08);
}

/* --------------------------------------------------
SIDEBAR
-------------------------------------------------- */

[data-testid="stSidebar"] {

    background: rgba(20,25,30,0.95);
}

/* --------------------------------------------------
SUCCESS / INFO BOXES
-------------------------------------------------- */

.stSuccess,
.stInfo,
.stWarning,
.stError {

    border-radius: 14px;
}

/* --------------------------------------------------
PROGRESS BAR
-------------------------------------------------- */

.stProgress > div > div > div > div {

    background-image: linear-gradient(
        90deg,
        #00c6ff,
        #0072ff
    );
}

</style>
""", unsafe_allow_html=True)
