"""
CyberShield AI
Auto Protection System

Purpose:
- Decide security action based on risk score
- Trigger Alert Manager for blocked/quarantined threats
"""

from alerts.alerts_manager import create_alert

def auto_response(
        threat_type,
        input_data,
        risk_score,
        reasons=None
):

    # Decide action
    if risk_score >= 80:
        action = "BLOCKED"

    elif risk_score >= 50:
        action = "QUARANTINED"

    else:
        action = "ALLOWED"


    # Generate alert for dangerous threats
    if action in ["BLOCKED", "QUARANTINED"]:

        if reasons is None:
            reasons = ["Suspicious activity detected"]

        create_alert(
            threat_type=threat_type,
            input_data=input_data,
            risk_score=risk_score,
            action=action,
            reasons=reasons
        )


    return {
        "risk_score": risk_score,
        "action": action
    }



# Testing
if __name__ == "__main__":

    test_result = auto_response(
        threat_type="PHISHING URL",
        input_data="http://sbi-login-verification.xyz",
        risk_score=85,
        reasons=[
            "Suspicious keyword: login",
            "No HTTPS security",
            "Fake banking domain"
        ]
    )


    print("Protection Result:")
    print(test_result)