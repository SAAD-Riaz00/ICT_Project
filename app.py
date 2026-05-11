# ------------------------------------------------------------
# PREMIUM MECHANICAL ENGINEERING THEME
# ------------------------------------------------------------

st.markdown("""
<style>

/* --------------------------------------------------------
MAIN BACKGROUND
-------------------------------------------------------- */

[data-testid="stAppViewContainer"]{
    background:
    linear-gradient(
        rgba(8,12,18,0.93),
        rgba(8,12,18,0.93)
    ),
    url("https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1920");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* --------------------------------------------------------
REMOVE DEFAULT STREAMLIT STYLING
-------------------------------------------------------- */

header{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* --------------------------------------------------------
MAIN CONTAINER
-------------------------------------------------------- */

.main .block-container{
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

/* --------------------------------------------------------
TITLE SECTION
-------------------------------------------------------- */

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:800;
    color:#ffffff;
    margin-bottom:10px;
    letter-spacing:1px;
}

.sub-title{
    text-align:center;
    font-size:18px;
    color:#c7d5e0;
    margin-bottom:30px;
    line-height:1.7;
}

/* --------------------------------------------------------
SECTION CARDS
-------------------------------------------------------- */

.section-card{

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 28px;

    margin-top: 15px;

    margin-bottom: 15px;

    box-shadow:
    0 8px 32px rgba(0,0,0,0.35);
}

/* --------------------------------------------------------
METRIC BOXES
-------------------------------------------------------- */

.metric-box{

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius:18px;

    padding:20px;

    text-align:center;

    margin-bottom:18px;

    backdrop-filter: blur(10px);

    transition:0.3s;
}

.metric-box:hover{

    transform: translateY(-3px);

    background: rgba(255,255,255,0.08);
}

/* --------------------------------------------------------
TEXT COLORS
-------------------------------------------------------- */

h1,h2,h3,h4,h5,h6,p,label,span{
    color:white !important;
}

/* --------------------------------------------------------
INPUT BOXES
-------------------------------------------------------- */

.stTextInput input,
.stNumberInput input{

    background-color: rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 12px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    padding: 10px !important;
}

/* --------------------------------------------------------
SELECT BOXES
-------------------------------------------------------- */

.stSelectbox div[data-baseweb="select"]{

    background-color: rgba(255,255,255,0.06) !important;

    border-radius: 12px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* --------------------------------------------------------
BUTTONS
-------------------------------------------------------- */

.stButton button{

    width:100%;

    background: linear-gradient(
        135deg,
        #2b5876,
        #4e4376
    );

    color:white;

    border:none;

    border-radius:14px;

    padding:12px;

    font-size:16px;

    font-weight:600;

    transition:0.3s;
}

.stButton button:hover{

    transform: scale(1.02);

    background: linear-gradient(
        135deg,
        #355c7d,
        #6c5b7b
    );
}

/* --------------------------------------------------------
TABS
-------------------------------------------------------- */

.stTabs [data-baseweb="tab-list"]{

    gap: 12px;
}

.stTabs [data-baseweb="tab"]{

    background: rgba(255,255,255,0.05);

    border-radius: 12px;

    padding: 12px 22px;

    color: white;

    font-weight: 600;

    border:1px solid rgba(255,255,255,0.05);
}

.stTabs [aria-selected="true"]{

    background: linear-gradient(
        135deg,
        #243b55,
        #141e30
    ) !important;

    border:1px solid rgba(255,255,255,0.1);
}

/* --------------------------------------------------------
DATAFRAME
-------------------------------------------------------- */

[data-testid="stDataFrame"]{

    background: rgba(255,255,255,0.05);

    border-radius: 18px;

    padding:10px;
}

/* --------------------------------------------------------
PROGRESS BAR
-------------------------------------------------------- */

.stProgress > div > div > div > div{

    background-image: linear-gradient(
        90deg,
        #11998e,
        #38ef7d
    );
}

/* --------------------------------------------------------
SIDEBAR
-------------------------------------------------------- */

[data-testid="stSidebar"]{

    background: rgba(15,20,25,0.95);
}

/* --------------------------------------------------------
SCROLLBAR
-------------------------------------------------------- */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#4e4376;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)
