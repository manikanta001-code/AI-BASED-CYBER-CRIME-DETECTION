"""
=========================================================
CyberShield AI

Cybercrime Detection & Digital Fraud Prevention System

Streamlit Dashboard

=========================================================
"""


import os
import sys
import streamlit as st



# ----------------------------------------------------
# Project Root
# ----------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


if PROJECT_ROOT not in sys.path:

    sys.path.insert(
        0,
        PROJECT_ROOT
    )



# ----------------------------------------------------
# Imports
# ----------------------------------------------------

from core.threat_analyzer import analyze_input



# ----------------------------------------------------
# Streamlit Configuration
# ----------------------------------------------------

st.set_page_config(

    page_title="CyberShield AI",

    page_icon="🛡️",

    layout="wide"

)



# ----------------------------------------------------
# Session Storage
# ----------------------------------------------------

if "latest_result" not in st.session_state:

    st.session_state.latest_result = None



# ----------------------------------------------------
# Theme
# ----------------------------------------------------

st.markdown(

"""
<style>


.main {

background-color:#0b1120;

}


h1,h2,h3 {

color:#00ff99;

}



.cyber-card {


background:#111827;


padding:20px;


border-radius:15px;


border:1px solid #374151;


text-align:center;


}



.card-title {


color:#9ca3af;


font-size:18px;


}



.card-value {


font-size:35px;


font-weight:bold;


color:white;


}



.stButton button {


background:#00ff99;


color:black;


font-weight:bold;


border-radius:10px;


}



</style>

""",

unsafe_allow_html=True

)

# ----------------------------------------------------
# Universal Threat Result Display
# ----------------------------------------------------

def show_result(result):


    # Save latest result

    st.session_state.latest_result = result



    st.markdown("---")


    st.subheader(
        "🛡 Threat Analysis Report"
    )



    # ------------------------------------------------
    # Risk Information
    # ------------------------------------------------


    score = result.get(

        "risk_score",

        0

    )


    level = result.get(

        "risk_level",

        "UNKNOWN"

    )


    action = result.get(

        "action",

        "UNKNOWN"

    )



    col1,col2,col3 = st.columns(3)



    col1.metric(

        "Risk Score",

        f"{score}/100"

    )



    col2.metric(

        "Risk Level",

        level

    )



    col3.metric(

        "Recommended Action",

        action

    )



    st.progress(

        min(

            score / 100,

            1.0

        )

    )



    # ------------------------------------------------
    # Status
    # ------------------------------------------------


    if level == "HIGH":


        st.error(

            "🚨 HIGH RISK THREAT DETECTED"

        )


    elif level == "MEDIUM":


        st.warning(

            "⚠️ SUSPICIOUS ACTIVITY DETECTED"

        )


    else:


        st.success(

            "✅ SAFE CONTENT"

        )



    # =================================================
    # IMAGE OCR RESULT
    # =================================================


    if "ocr_text" in result:


        st.markdown("---")


        st.subheader(

            "📝 OCR Extracted Text"

        )


        text = result.get(

            "ocr_text",

            ""

        )



        if text:


            st.text_area(

                "Detected Text",

                text,

                height=150

            )


        else:


            st.info(

                "No text detected in image"

            )



    # =================================================
    # OCR SCAM ANALYSIS
    # =================================================


    if "scam_result" in result:


        st.subheader(

            "🚨 OCR Scam Analysis"

        )


        st.write(

            result["scam_result"]

        )



    # =================================================
    # AI IMAGE DETECTION
    # =================================================


    if "ai_detection" in result:


        st.subheader(

            "🤖 AI Image Detection"

        )


        st.write(

            result["ai_detection"]

        )



    # =================================================
    # METADATA
    # =================================================


    if "metadata" in result:


        st.subheader(

            "📷 Metadata Analysis"

        )


        st.write(

            result["metadata"]

        )



    # =================================================
    # ELA
    # =================================================


    if "ela" in result:


        st.subheader(

            "🔍 Error Level Analysis (ELA)"

        )


        st.write(

            result["ela"]

        )



    # =================================================
    # Reasons
    # =================================================


    st.markdown("---")


    st.subheader(

        "📌 Detection Reasons"

    )



    reasons = result.get(

        "reasons",

        []

    )



    if reasons:


        for reason in reasons:


            st.write(

                "•",

                reason

            )


    else:


        st.info(

            "No additional reasons available"

        )

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.markdown(
"""
# 🛡 CyberShield AI

### Cybercrime Detection Platform

AI-powered fraud prevention system

---
"""
)



page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📩 Scam Detector",

        "🌐 URL Scanner",

        "📧 Email Checker",

        "🖼 Image Scanner"

    ]

)



st.sidebar.markdown(
"""
---

## System Status

🟢 Scam Detection

🟢 URL Detection

🟢 Email Security

🟢 OCR Analysis

🟢 AI Image Detection

🟢 Risk Engine


---

CyberShield AI

Hackathon Demo

"""
)



# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

if page == "🏠 Dashboard":


    st.title(

        "🛡 CyberShield AI"

    )


    st.subheader(

        "AI Powered Cybercrime Detection & Digital Fraud Prevention"

    )



    st.success(

        "🟢 System Online - Ready For Threat Analysis"

    )



    st.markdown("---")



    col1,col2,col3 = st.columns(3)



    with col1:


        st.markdown(

        """
        <div class="cyber-card">

        <div class="card-title">

        Detection Engines

        </div>


        <div class="card-value">

        5+

        </div>

        </div>
        """,

        unsafe_allow_html=True

        )



    with col2:


        st.markdown(

        """
        <div class="cyber-card">

        <div class="card-title">

        AI Modules

        </div>


        <div class="card-value">

        4

        </div>

        </div>
        """,

        unsafe_allow_html=True

        )



    with col3:


        st.markdown(

        """
        <div class="cyber-card">

        <div class="card-title">

        Status

        </div>


        <div class="card-value">

        LIVE

        </div>

        </div>
        """,

        unsafe_allow_html=True

        )



    st.markdown("---")



    st.subheader(

        "🚀 Security Modules"

    )



    c1,c2,c3 = st.columns(3)



    c1.info(

"""
### 📩 Scam Detection

Detect fraudulent SMS/messages.

AI:

TF-IDF + SVM
"""
    )



    c2.info(

"""
### 🌐 URL Scanner

Detect:

• Phishing
• Fake domains
• Impersonation
"""
    )



    c3.info(

"""
### 📧 Email Security

Check:

• Domain
• SPF
• DKIM
• DMARC
"""
    )



    c4,c5,c6 = st.columns(3)



    c4.info(

"""
### 🖼 Image Analysis

OCR

AI Detection

Scam Detection
"""
    )



    c5.info(

"""
### 🔍 Image Forensics

Metadata

ELA

Manipulation Check
"""
    )



    c6.info(

"""
### ⚡ Risk Engine

Combines all threats
into final score.
"""
    )



    st.markdown("---")



    if st.session_state.latest_result:


        st.subheader(

            "Latest Scan"

        )


        st.write(

            st.session_state.latest_result

        )


    else:


        st.info(

            "No scan performed yet."

        )




# ----------------------------------------------------
# Scam Detector
# ----------------------------------------------------

elif page == "📩 Scam Detector":


    st.title(

        "📩 Scam Message Detection"

    )



    message = st.text_area(

        "Enter Message",

        height=150

    )



    if st.button(

        "Analyze Message"

    ):


        if message.strip()=="":


            st.warning(

                "Enter message"

            )


        else:


            result = analyze_input(

                message,

                "text"

            )


            show_result(

                result

            )




# ----------------------------------------------------
# URL Scanner
# ----------------------------------------------------

elif page == "🌐 URL Scanner":


    st.title(

        "🌐 Phishing URL Scanner"

    )


    url = st.text_input(

        "Enter URL"

    )



    if st.button(

        "Analyze URL"

    ):


        if url.strip()=="":


            st.warning(

                "Enter URL"

            )


        else:


            result = analyze_input(

                url,

                "url"

            )


            show_result(

                result

            )





# ----------------------------------------------------
# Email Checker
# ----------------------------------------------------

elif page == "📧 Email Checker":


    st.title(

        "📧 Email Fraud Detection"

    )



    email = st.text_input(

        "Enter Email"

    )



    if st.button(

        "Analyze Email"

    ):


        if email.strip()=="":


            st.warning(

                "Enter Email"

            )


        else:


            result = analyze_input(

                email,

                "email"

            )


            show_result(

                result

            )

# ----------------------------------------------------
# Image Scanner
# ----------------------------------------------------

elif page == "🖼 Image Scanner":


    st.title(

        "🖼 Image Fraud Detection"

    )


    st.write(

"""
Analyze images using:

• OCR Text Extraction

• Scam Text Detection

• AI Generated Image Detection

• Metadata Analysis

• Error Level Analysis (ELA)

"""
    )



    uploaded = st.file_uploader(

        "Upload Image",

        type=[

            "png",

            "jpg",

            "jpeg"

        ]

    )



    if uploaded:


        os.makedirs(

            "temp",

            exist_ok=True

        )



        image_path = os.path.join(

            "temp",

            uploaded.name

        )



        with open(

            image_path,

            "wb"

        ) as file:


            file.write(

                uploaded.getbuffer()

            )



        st.image(

            uploaded,

            width=450

        )



        if st.button(

            "Analyze Image"

        ):


            with st.spinner(

                "Analyzing Image..."

            ):


                result = analyze_input(

                    image_path,

                    "image"

                )



            show_result(

                result

            )

