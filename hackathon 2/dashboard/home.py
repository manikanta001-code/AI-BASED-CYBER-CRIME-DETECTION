"""
CyberShield AI Home
"""

import streamlit as st


def show_home():

    st.title("🛡️ CyberShield AI")

    st.subheader(
        "Cybercrime Detection & Digital Fraud Prevention System"
    )


    st.write(
        """
        AI powered security platform to detect:

        ✅ Scam Messages

        ✅ Phishing URLs

        ✅ Suspicious Activities

        ✅ Automated Protection

        ✅ Threat Alerts
        """
    )


    st.divider()


    c1,c2,c3 = st.columns(3)


    with c1:
        st.metric(
            "Scam Detection",
            "Active"
        )

    with c2:
        st.metric(
            "Phishing Detection",
            "Active"
        )

    with c3:
        st.metric(
            "Alert System",
            "Active"
        )