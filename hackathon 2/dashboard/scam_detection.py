"""
CyberShield AI
Scam Detection Dashboard
"""

import streamlit as st

from models.scam_detector import predict


def show_scam_detection():

    st.title("📱 Scam Message Detection")


    message = st.text_area(
        "Enter SMS / Email message"
    )


    if st.button("Analyze"):

        if message.strip() == "":
            st.warning("Enter a message")
            return


        # use existing predict.py function
        result = predict.predict_message(message)


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