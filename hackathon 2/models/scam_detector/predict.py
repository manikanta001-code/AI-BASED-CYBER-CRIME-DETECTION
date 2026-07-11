"""
CyberShield AI
Scam Detection Prediction Module

Uses:
- TF-IDF Vectorizer
- Linear SVM Model
- Rule Based Risk Engine

Input:
Text message

Output:
Prediction + Risk Score + Explanation
"""


import os
import re
import joblib



# ---------------------------------
# Model Paths
# ---------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)


VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "vectorizer.pkl"
)



# ---------------------------------
# Load ML Model
# ---------------------------------

model = joblib.load(
    MODEL_PATH
)


vectorizer = joblib.load(
    VECTORIZER_PATH
)



# ---------------------------------
# Rule Based Keywords
# ---------------------------------

SCAM_KEYWORDS = [

    "click here",
    "verify",
    "kyc",
    "otp",
    "password",
    "bank account",
    "won",
    "winner",
    "prize",
    "reward",
    "claim",
    "urgent",
    "limited time",
    "free money",
    "lottery",
    "refund"

]



# ---------------------------------
# Text Cleaning
# ---------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()



# ---------------------------------
# Prediction Function
# ---------------------------------

def predict_message(message):


    cleaned = clean_text(
        message
    )


    reasons = []



    # -----------------------------
    # ML Prediction
    # -----------------------------

    vector = vectorizer.transform(
        [cleaned]
    )


    prediction = model.predict(
        vector
    )[0]



    # -----------------------------
    # Rule Detection
    # -----------------------------

    keyword_count = 0


    for word in SCAM_KEYWORDS:

        if word in cleaned:

            keyword_count += 1

            reasons.append(
                f"Keyword detected: {word}"
            )



    # -----------------------------
    # Risk Calculation
    # -----------------------------

    if prediction == 1:

        risk_score = 70

    else:

        risk_score = 10



    # Increase risk based on keywords

    risk_score += keyword_count * 5



    if risk_score > 100:

        risk_score = 100



    # -----------------------------
    # Final Result
    # -----------------------------

    if risk_score >= 70:

        final_prediction = "SCAM"

        risk_level = "HIGH"


    elif risk_score >= 40:

        final_prediction = "SUSPICIOUS"

        risk_level = "MEDIUM"


    else:

        final_prediction = "SAFE"

        risk_level = "LOW"



    return {


        "prediction":
            final_prediction,


        "risk_score":
            risk_score,


        "risk_level":
            risk_level,


        "reasons":
            reasons

    }



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":


    msg = """
    Congratulations!
    You won Rs 50000.
    Click here to claim your reward.
    """


    result = predict_message(
        msg
    )


    print(result)