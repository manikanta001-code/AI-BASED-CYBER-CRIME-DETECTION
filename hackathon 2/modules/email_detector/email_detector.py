"""
CyberShield AI
Email Threat Detection Engine

Input:
Email Address

Checks:
- Domain Analysis
- Reputation
- SPF/DKIM/DMARC
- Risk Calculation
"""


from .domain_analysis import analyze_domain
from .reputation import check_reputation
from .spf_dkim_dmarc import check_email_security
from .email_checker import validate_email



def analyze_email(email):


    # -----------------------------
    # Validate Email
    # -----------------------------

    if not validate_email(email):

        return {

            "email": email,

            "risk_score":100,

            "risk_level":"HIGH",

            "action":"BLOCK",

            "reasons":[
                "Invalid email format"
            ]

        }



    # -----------------------------
    # Domain Analysis
    # -----------------------------

    domain_result = analyze_domain(email)


    domain = domain_result["domain"]



    # -----------------------------
    # Reputation
    # -----------------------------

    reputation_result = check_reputation(
        domain
    )



    # -----------------------------
    # Security Records
    # -----------------------------

    security_result = check_email_security(
        domain
    )



    # -----------------------------
    # Final Risk
    # -----------------------------

    risk_score = (

        domain_result["domain_risk"]

        +

        reputation_result["reputation_risk"]

        +

        security_result["security_score"]

    )



    risk_score = min(
        risk_score,
        100
    )



    if risk_score >= 70:

        risk_level = "HIGH"

        action = "BLOCK"



    elif risk_score >=40:

        risk_level = "MEDIUM"

        action = "REVIEW"



    else:

        risk_level = "LOW"

        action = "ALLOW"



    reasons = (

        domain_result["reasons"]

        +

        reputation_result["reasons"]

        +

        security_result["reasons"]

    )



    return {


        "email":email,


        "risk_score":risk_score,


        "risk_level":risk_level,


        "action":action,


        "reasons":reasons

    }