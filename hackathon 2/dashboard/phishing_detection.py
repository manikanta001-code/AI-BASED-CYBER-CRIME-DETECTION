"""
CyberShield AI
Phishing URL Dashboard
"""

import streamlit as st

from models.phishing_url import predict


def show_phishing_detection():

    st.title("🌐 Phishing URL Detection")


    url = st.text_input(
        "Enter URL"
    )


    if st.button("Analyze URL"):


        if url.strip() == "":
            st.warning("Enter URL")
            return


        result = predict.predict_url(url)


        st.subheader("Result")


        if isinstance(result, dict):

            st.write(
                "**Prediction:**",
                result.get("prediction")
            )

            st.write(
                "**Risk Score:**",
                result.get("risk_score")
            )


            st.write("**Reasons:**")

            for r in result.get("reasons", []):
                st.write("•", r)

        else:

            st.write(result)