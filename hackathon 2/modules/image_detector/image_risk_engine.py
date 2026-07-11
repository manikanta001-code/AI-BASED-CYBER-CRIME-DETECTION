"""
CyberShield AI
Image Risk Engine
"""

def calculate_image_risk(
    ocr_result,
    ai_result,
    metadata_result,
    ela_result
):

    total_score = 0
    reasons = []

    # ----------------------------
    # OCR Scam Detection
    # ----------------------------

    ocr_score = (
        ocr_result
        .get("scam_analysis", {})
        .get("risk_score", 0)
    )

    total_score += ocr_score * 0.50

    if ocr_score >= 50:

        reasons.append(
            "Suspicious text detected by OCR"
        )

    # ----------------------------
    # AI Detection
    # ----------------------------

    ai_score = ai_result.get(
        "risk_score",
        0
    )

    total_score += ai_score * 0.20

    if ai_score >= 50:

        reasons.append(
            "AI generated image detected"
        )

    # ----------------------------
    # Metadata
    # ----------------------------

    metadata_score = metadata_result.get(
        "risk_score",
        0
    )

    total_score += metadata_score * 0.15

    if metadata_score >= 20:

        reasons.append(
            "Suspicious metadata detected"
        )

    # ----------------------------
    # ELA
    # ----------------------------

    ela_score = ela_result.get(
        "risk_score",
        0
    )

    total_score += ela_score * 0.15

    if ela_score >= 20:

        reasons.append(
            "Possible image manipulation"
        )

    # ----------------------------
    # Final Score
    # ----------------------------

    final_score = round(
        min(total_score, 100)
    )

    if final_score >= 70:

        level = "HIGH"
        action = "BLOCK"

    elif final_score >= 40:

        level = "MEDIUM"
        action = "REVIEW"

    else:

        level = "LOW"
        action = "ALLOW"

    return {

        "risk_score": final_score,

        "risk_level": level,

        "action": action,

        "reasons": reasons

    }