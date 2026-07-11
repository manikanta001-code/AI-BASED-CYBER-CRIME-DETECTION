"""
CyberShield AI
Phishing URL Prediction Module

Input:
URL

Output:
Prediction
Risk Score
Reasons
"""

import os
import sys
import re
import joblib
import tldextract


# ---------------------------------
# Add Project Root
# ---------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

sys.path.append(PROJECT_ROOT)


from config import BASE_DIR



# ---------------------------------
# Model Path
# ---------------------------------

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "phishing_url",
    "phishing_url_model.pkl"
)


# Load model

model = joblib.load(
    MODEL_PATH
)



# ---------------------------------
# Feature Extraction
# ---------------------------------

def extract_features(url):

    url = str(url).lower()

    extracted = tldextract.extract(url)

    features = []


    # URL length

    features.append(
        len(url)
    )


    # Dots

    features.append(
        url.count(".")
    )


    # Hyphens

    features.append(
        url.count("-")
    )


    # Digits

    features.append(
        sum(
            c.isdigit()
            for c in url
        )
    )


    # HTTPS

    features.append(
        1 if url.startswith("https") else 0
    )


    # IP address

    ip_pattern = r"\d+\.\d+\.\d+\.\d+"

    features.append(
        1 if re.search(ip_pattern,url) else 0
    )


    # Suspicious keywords

    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "kyc",
        "free",
        "gift",
        "winner",
        "claim"
    ]


    count = 0

    for word in suspicious_words:

        if word in url:

            count += 1


    features.append(
        count
    )


    # Domain length

    features.append(
        len(extracted.domain)
    )


    return features



# ---------------------------------
# Rule Engine
# ---------------------------------

def url_rules(url):

    score = 0

    reasons = []


    url_lower = url.lower()


    keywords = [
        "login",
        "verify",
        "update",
        "bank",
        "kyc",
        "winner",
        "gift",
        "claim"
    ]


    for word in keywords:

        if word in url_lower:

            score += 10

            reasons.append(
                f"Suspicious keyword: {word}"
            )


    if "-" in url:

        score += 10

        reasons.append(
            "Multiple hyphens in domain"
        )


    if not url.startswith("https"):

        score += 15

        reasons.append(
            "No HTTPS security"
        )


    return score, reasons



# ---------------------------------
# Prediction Function
# ---------------------------------

def predict_url(url):


    features = extract_features(
        url
    )


    prediction = model.predict(
        [features]
    )[0]


    # Rules

    rule_score, reasons = url_rules(
        url
    )


    risk_score = rule_score


    if prediction == 1:

        result = "PHISHING"

        risk_score += 50

    else:

        result = "SAFE"

        risk_score += 5



    risk_score = min(
        risk_score,
        100
    )


    return {

        "prediction": result,

        "risk_score": risk_score,

        "reasons": reasons

    }



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":


    while True:

        url = input(
            "\nEnter URL (exit): "
        )


        if url.lower()=="exit":
            break


        result = predict_url(
            url
        )


        print("\nResult:")
        print(result)