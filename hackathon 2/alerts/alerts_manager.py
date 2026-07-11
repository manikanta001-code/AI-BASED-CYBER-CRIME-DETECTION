"""
CyberShield AI
Alert Manager Module

Purpose:
- Generate alerts
- Store evidence
- Save threat history
- Maintain quarantine records
"""


import json
import os
from datetime import datetime



# Alert storage file

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


ALERT_FILE = os.path.join(
    BASE_DIR,
    "quarantine.json"
)



# -----------------------------------
# Create Alert Function
# -----------------------------------

def create_alert(
        threat_type,
        input_data,
        risk_score,
        action,
        reasons
):


    alert = {

        "time":
            str(datetime.now()),


        "threat_type":
            threat_type,


        "input":
            input_data,


        "risk_score":
            risk_score,


        "action":
            action,


        "reasons":
            reasons

    }



    # Ensure alerts folder exists

    os.makedirs(
        BASE_DIR,
        exist_ok=True
    )



    # Load old alerts

    if os.path.exists(ALERT_FILE):

        try:

            with open(
                ALERT_FILE,
                "r"
            ) as file:

                alerts = json.load(file)


        except json.JSONDecodeError:

            alerts = []


    else:

        alerts = []



    # Add new alert

    alerts.append(
        alert
    )



    # Save alerts

    with open(
        ALERT_FILE,
        "w"
    ) as file:

        json.dump(
            alerts,
            file,
            indent=4
        )



    return alert




# -----------------------------------
# Direct Testing
# -----------------------------------

if __name__ == "__main__":


    result = create_alert(

        threat_type="SCAM SMS",

        input_data=
        "Your bank account blocked. Click KYC link",

        risk_score=90,

        action="BLOCKED",

        reasons=[

            "Urgent message",

            "Suspicious link"

        ]

    )


    print(
        "Alert Generated:"
    )

    print(
        result
    )