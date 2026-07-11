"""
CyberShield AI
Email Domain Analysis Module

Checks:
- Suspicious domain keywords
- Brand impersonation
- Character substitution attacks
- Free email providers
- Domain existence
"""

import socket


# Suspicious words commonly used in phishing domains

SUSPICIOUS_KEYWORDS = [

    "login",
    "verify",
    "secure",
    "security",
    "update",
    "account",
    "support",
    "alert",
    "bank",
    "wallet",
    "payment",
    "confirm"

]


# Common trusted brands targeted by attackers

BRANDS = [

    "paypal",
    "amazon",
    "microsoft",
    "google",
    "apple",
    "sbi",
    "icici",
    "netflix"

]


# Free email services

FREE_EMAIL_DOMAINS = [

    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com"

]



def extract_domain(email):

    """
    Extract domain from email address
    """

    return email.split("@")[-1].lower()




def analyze_domain(email):

    domain = extract_domain(email)

    risk = 0

    reasons = []


    # ---------------------------------
    # Suspicious keyword detection
    # ---------------------------------

    for word in SUSPICIOUS_KEYWORDS:

        if word in domain:

            risk += 15

            reasons.append(
                f"Suspicious keyword found: {word}"
            )



    # ---------------------------------
    # Brand impersonation detection
    # ---------------------------------

    for brand in BRANDS:


        if brand in domain:


            # Example:
            # paypa1-login.com

            if domain != brand + ".com":


                risk += 30


                reasons.append(

                    f"Possible {brand} impersonation"

                )



    # ---------------------------------
    # Character substitution attack
    # ---------------------------------

    if "1" in domain or "0" in domain:


        risk += 25


        reasons.append(

            "Possible brand impersonation using numbers"

        )



    # ---------------------------------
    # Free email provider check
    # ---------------------------------

    if domain in FREE_EMAIL_DOMAINS:


        risk += 5


        reasons.append(

            "Free email provider used"

        )



    # ---------------------------------
    # Domain existence check
    # ---------------------------------

    try:

        socket.gethostbyname(domain)


    except:


        risk += 30


        reasons.append(

            "Domain does not exist"

        )



    return {


        "domain": domain,


        "domain_risk": min(risk,100),


        "reasons": reasons

    }