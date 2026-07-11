import sys
import os


# Add project root
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    PROJECT_ROOT
)


from modules.image_detector.ocr_scam_detector import analyze_image_for_scam



image = "test_images/scam.png"



result = analyze_image_for_scam(
    image
)



print("\n========== OCR TEXT ==========")
print(
    result["extracted_text"]
)



print("\n========== CLEANED TEXT ==========")
print(
    result["cleaned_text"]
)



print("\n========== SCAM RESULT ==========")
print(
    result["scam_analysis"]
)