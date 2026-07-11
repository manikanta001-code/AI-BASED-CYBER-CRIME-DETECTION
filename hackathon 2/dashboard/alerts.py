"""
CyberShield AI
Alerts Dashboard Module
"""

import streamlit as st
import json
import os


ALERT_FILE = "alerts/quarantine.json"


def load_alerts():

    if os.path.exists(ALERT_FILE):

        with open(ALERT_FILE, "r") as file:
            return json.load(file)

    return []


def show_alerts():

    st.title("⚠ CyberShield AI - Threat Alerts")


    alerts = load_alerts()


    if len(alerts) == 0:

        st.success("No threats detected")

        return


    # Summary
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Threats",
            len(alerts)
        )

    with col2:

        blocked = len(
            [
                a for a in alerts
                if a.get("action") == "BLOCKED"
            ]
        )

        st.metric(
            "Blocked Threats",
            blocked
        )


    st.divider()


    # Display alerts
    for index, alert in enumerate(reversed(alerts), 1):

        st.subheader(
            f"🚨 Threat {index}"
        )


        threat_type = (
            alert.get("threat_type")
            or
            alert.get("type")
            or
            "Unknown Threat"
        )


        input_data = (
            alert.get("input")
            or
            alert.get("content")
            or
            "No data"
        )


        st.write(
            "**Threat Type:**",
            threat_type
        )


        st.write(
            "**Input:**",
            input_data
        )


        st.write(
            "**Risk Score:**",
            alert.get("risk_score", 0)
        )


        action = alert.get(
            "action",
            "UNKNOWN"
        )


        if action == "BLOCKED":

            st.error(
                f"Action: {action}"
            )

        elif action == "QUARANTINED":

            st.warning(
                f"Action: {action}"
            )

        else:

            st.info(
                f"Action: {action}"
            )


        # Reasons
        if "reasons" in alert:

            st.write("**Reasons:**")

            for reason in alert["reasons"]:

                st.write(
                    "•",
                    reason
                )


        st.caption(
            "Time: " + alert.get("time", "Unknown")
        )

        st.divider()



if __name__ == "__main__":

    show_alerts()