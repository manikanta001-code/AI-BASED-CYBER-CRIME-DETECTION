"""
CyberShield AI
Central Risk Engine

Combines:
- Scam Detection Risk
- Phishing URL Risk
- Fake Identity Risk
- Auto Protection Decision
"""


# ---------------------------------
# Calculate Final Risk Score
# ---------------------------------

def calculate_risk(
        scam_score=0,
        phishing_score=0,
        identity_score=0
):

    """
    Weighted Risk Calculation

    Scam       : 40%
    Phishing   : 40%
    Identity   : 20%
    """


    final_score = (

        scam_score * 0.40

        +

        phishing_score * 0.40

        +

        identity_score * 0.20

    )


    final_score = round(
        final_score
    )


    # Risk Level

    if final_score >= 80:

        level = "CRITICAL"

        action = "BLOCKED"


    elif final_score >= 50:

        level = "HIGH"

        action = "QUARANTINED"


    elif final_score >= 30:

        level = "MEDIUM"

        action = "MONITORED"


    else:

        level = "LOW"

        action = "ALLOWED"



    return {

        "final_risk_score": final_score,

        "risk_level": level,

        "recommended_action": action

    }



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":


    result = calculate_risk(

        scam_score=76,

        phishing_score=85,

        identity_score=40

    )


    print(result)