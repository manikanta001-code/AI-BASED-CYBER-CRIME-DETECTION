"""
CyberShield AI

AI Image Detector
"""

from modules.image_detector.api.sightengine_api import analyze_ai_image


def detect_ai_image(image_path):

    try:

        response = analyze_ai_image(image_path)

        # Your API function returns:
        # (response_json, status_code)
        data = response[0]

        ai_probability = (
            data.get("type", {})
                .get("ai_generated", 0)
        )

        if ai_probability >= 0.90:

            return {

                "prediction": "AI GENERATED IMAGE",

                "ai_probability": ai_probability,

                "risk_score": 90,

                "reasons": [

                    "Very high AI generation probability"

                ]

            }

        elif ai_probability >= 0.60:

            return {

                "prediction": "LIKELY AI GENERATED",

                "ai_probability": ai_probability,

                "risk_score": 60,

                "reasons": [

                    "Moderate AI generation probability"

                ]

            }

        elif ai_probability >= 0.30:

            return {

                "prediction": "POSSIBLY AI GENERATED",

                "ai_probability": ai_probability,

                "risk_score": 30,

                "reasons": [

                    "Low AI generation probability"

                ]

            }

        else:

            return {

                "prediction": "ORIGINAL CAMERA IMAGE",

                "ai_probability": ai_probability,

                "risk_score": 5,

                "reasons": [

                    "Very low AI generation probability"

                ]

            }

    except Exception as e:

        return {

            "prediction": "UNKNOWN",

            "ai_probability": 0,

            "risk_score": 0,

            "reasons": [

                str(e)

            ]

        }