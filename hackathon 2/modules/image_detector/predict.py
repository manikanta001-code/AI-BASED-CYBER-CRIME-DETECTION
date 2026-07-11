from modules.image_detector.api.sightengine_api import analyze_ai_image


def predict_image(image_path):
    result = analyze_ai_image(image_path)

    if result.get("status") != "success":
        return {
            "status": "error",
            "message": result
        }

    ai_score = result["type"]["ai_generated"]

    confidence = round(ai_score * 100, 2)

    if ai_score < 0.20:
        prediction = "ORIGINAL CAMERA IMAGE"
        risk = 5
        explanation = "Image appears to be captured by a real camera."

    elif ai_score < 0.60:
        prediction = "UNCERTAIN"
        risk = 50
        explanation = "Image has mixed characteristics. Manual verification recommended."

    else:
        prediction = "AI GENERATED IMAGE"
        risk = 95
        explanation = "Image is highly likely to be AI generated."

    return {
        "prediction": prediction,
        "confidence": confidence,
        "risk_score": risk,
        "explanation": explanation,
        "raw_api": result
    }