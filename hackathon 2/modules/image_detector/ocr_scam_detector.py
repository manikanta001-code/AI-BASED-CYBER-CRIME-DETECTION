"""
CyberShield AI

OCR + Scam Detection Integration

Image
 |
 OCR
 |
 Text Cleaning
 |
 Scam Detection
 |
 Result
"""


import re

from modules.image_detector.ocr_reader import extract_text
from models.scam_detector.predict import predict_message



# -----------------------------
# Clean OCR Text
# -----------------------------

def clean_text(text):

    if not text:
        return ""

    text = text.replace(
        "\n",
        " "
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()



# -----------------------------
# Main Function
# -----------------------------

def analyze_image_for_scam(file_path):


    # OCR
    extracted_text = extract_text(
        file_path
    )


    # Clean text
    cleaned_text = clean_text(
        extracted_text
    )


    # If no text
    if cleaned_text == "":

        return {

            "extracted_text": "",

            "cleaned_text": "",

            "scam_analysis": {

                "prediction": "UNKNOWN",

                "risk_score": 0,

                "risk_level": "LOW",

                "reasons": [
                    "No text detected"
                ]

            }

        }



    # Scam detection
    scam_result = predict_message(
        cleaned_text
    )



    return {


        "extracted_text":
            extracted_text,


        "cleaned_text":
            cleaned_text,


        "scam_analysis":
            scam_result

    }