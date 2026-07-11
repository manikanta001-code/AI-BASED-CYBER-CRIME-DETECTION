"""
CyberShield AI
URL Risk Engine
"""

from models.phishing_url.url_validator import validate_url
from models.phishing_url.domain_analysis import analyze_domain
from models.phishing_url.virustotal_api import scan_url


def analyze_url(url):

    # -------------------------
    # Validate URL
    # -------------------------

    validation = validate_url(url)

    if not validation["valid"]:

        return {

            "url": url,

            "risk_score": 100,

            "risk_level": "HIGH",

            "action": "BLOCK",

            "reasons": [
                "Invalid URL"
            ]
        }

    total_risk = 0
    reasons = []

    # -------------------------
    # HTTPS Check
    # -------------------------

    if validation["scheme"] == "http":

        total_risk += 20

        reasons.append(
            "URL is not using HTTPS"
        )

    # -------------------------
    # Domain Analysis
    # -------------------------

    domain_result = analyze_domain(
        validation["domain"]
    )

    total_risk += domain_result["risk_score"]

    reasons.extend(
        domain_result["reasons"]
    )

    # -------------------------
    # VirusTotal
    # -------------------------

    vt = scan_url(url)

    if vt["success"]:

        # Only add risk if VirusTotal actually found something
        if vt["malicious"] > 0:

            total_risk += 80

            reasons.append(
                f"VirusTotal: {vt['malicious']} vendors marked this URL malicious."
            )

        elif vt["suspicious"] > 0:

            total_risk += 40

            reasons.append(
                f"VirusTotal: {vt['suspicious']} vendors marked this URL suspicious."
            )

    else:

        reasons.append(
            "VirusTotal scan unavailable."
        )

    # -------------------------
    # Limit
    # -------------------------

    total_risk = min(total_risk, 100)

    # -------------------------
    # Final Decision
    # -------------------------

    if total_risk >= 70:

        level = "HIGH"
        action = "BLOCK"

    elif total_risk >= 40:

        level = "MEDIUM"
        action = "REVIEW"

    else:

        level = "LOW"
        action = "ALLOW"

    return {

        "url": url,

        "risk_score": total_risk,

        "risk_level": level,

        "action": action,

        "reasons": reasons

    }


if __name__ == "__main__":

    url = input("Enter URL: ")

    print(analyze_url(url))