"""
CyberShield AI
Complete Image Analyzer
"""

from modules.image_detector.ocr_scam_detector import analyze_image_for_scam
from modules.image_detector.ai_detector import detect_ai_image
from modules.image_detector.metadata import analyze_metadata
from modules.image_detector.ela import analyze_ela
from modules.image_detector.image_risk_engine import calculate_image_risk

from alerts.alerts_manager import create_alert


def analyze_image(image_path):

    # OCR + Scam Detection

    ocr_result = analyze_image_for_scam(image_path)

    # AI Detection

    ai_result = detect_ai_image(image_path)

    # Metadata

    metadata_result = analyze_metadata(image_path)

    # ELA

    ela_result = analyze_ela(image_path)

    # Final Risk

    final_result = calculate_image_risk(

        ocr_result,

        ai_result,

        metadata_result,

        ela_result

    )

    # Alert

    if final_result["risk_level"] == "HIGH":

        create_alert(

            threat_type="IMAGE FRAUD",

            input_data=image_path,

            risk_score=final_result["risk_score"],

            action=final_result["action"],

            reasons=final_result["reasons"]

        )

    return {

        "ocr_text": ocr_result.get(
            "cleaned_text",
            ""
        ),

        "scam_result": ocr_result.get(
            "scam_analysis",
            {}
        ),

        "ai_detection": ai_result,

        "metadata": metadata_result,

        "ela": ela_result,

        "risk_score": final_result["risk_score"],

        "risk_level": final_result["risk_level"],

        "action": final_result["action"],

        "reasons": final_result["reasons"]

    }


if __name__ == "__main__":

    image = "test_images/scam.png"

    print(analyze_image(image))