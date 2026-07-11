import sys
import os


# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    PROJECT_ROOT
)


from modules.image_detector.image_risk_engine import calculate_image_risk



# -----------------------------
# Mock Module Results
# -----------------------------

ocr_result = {

    "scam_analysis": {

        "prediction": "SCAM",

        "risk_score": 90,

        "risk_level": "HIGH"

    }

}



ai_result = {

    "prediction": "ORIGINAL",

    "risk_score": 10

}



metadata_result = {

    "camera": "Unknown",

    "risk_score": 20

}



ela_result = {

    "prediction": "LIKELY ORIGINAL",

    "risk_score": 5

}



# -----------------------------
# Calculate Final Risk
# -----------------------------

result = calculate_image_risk(

    ocr_result,

    ai_result,

    metadata_result,

    ela_result

)



print("\n========== IMAGE RISK RESULT ==========")

print(result)