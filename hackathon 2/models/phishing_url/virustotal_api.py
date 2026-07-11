"""
CyberShield AI
VirusTotal URL Scanner
"""

import time
import requests

from models.phishing_url.config import VIRUSTOTAL_API_KEY


BASE_URL = "https://www.virustotal.com/api/v3"


def scan_url(url):

    if not VIRUSTOTAL_API_KEY:

        return {
            "success": False,
            "error": "VirusTotal API key not found."
        }

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    # ----------------------------
    # Submit URL
    # ----------------------------

    submit = requests.post(
        f"{BASE_URL}/urls",
        headers=headers,
        data={"url": url}
    )

    if submit.status_code != 200:

        return {
            "success": False,
            "error": submit.text
        }

    analysis_id = submit.json()["data"]["id"]

    # ----------------------------
    # Wait for analysis completion
    # ----------------------------

    data = None

    for _ in range(15):

        time.sleep(2)

        report = requests.get(
            f"{BASE_URL}/analyses/{analysis_id}",
            headers=headers
        )

        if report.status_code != 200:
            continue

        data = report.json()["data"]["attributes"]

        if data["status"] == "completed":
            break

    if data is None:

        return {
            "success": False,
            "error": "Unable to retrieve analysis."
        }

    stats = data.get("stats", {})

    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)
    harmless = stats.get("harmless", 0)
    undetected = stats.get("undetected", 0)

    # ----------------------------
    # Risk Score
    # ----------------------------

    risk_score = min(
        malicious * 25 +
        suspicious * 15,
        100
    )

    if risk_score >= 70:

        level = "HIGH"

        action = "BLOCK"

    elif risk_score >= 40:

        level = "MEDIUM"

        action = "REVIEW"

    else:

        level = "LOW"

        action = "ALLOW"

    reasons = []

    if malicious:
        reasons.append(
            f"{malicious} security vendors marked this URL as malicious."
        )

    if suspicious:
        reasons.append(
            f"{suspicious} vendors marked this URL as suspicious."
        )

    if not reasons:
        reasons.append(
            "No security vendors detected malicious activity."
        )

    return {

        "success": True,

        "url": url,

        "risk_score": risk_score,

        "risk_level": level,

        "action": action,

        "malicious": malicious,

        "suspicious": suspicious,

        "harmless": harmless,

        "undetected": undetected,

        "stats": stats,

        "reasons": reasons

    }


if __name__ == "__main__":

    url = input("Enter URL: ")

    result = scan_url(url)

    print("\nRESULT")
    print(result)