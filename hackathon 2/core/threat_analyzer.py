"""
CyberShield AI

Unified Threat Analyzer
"""

from models.scam_detector.predict import predict_message

from modules.email_detector.email_detector import analyze_email

from models.phishing_url.url_risk_engine import analyze_url

from modules.image_detector.image_analyzer import analyze_image


def analyze_input(input_data, input_type):

    input_type = input_type.lower()

    if input_type == "text":

        return predict_message(input_data)

    elif input_type == "url":

        return analyze_url(input_data)

    elif input_type == "email":

        return analyze_email(input_data)

    elif input_type == "image":

        return analyze_image(input_data)

    else:

        return {

            "error": "Unsupported input type"

        }


if __name__ == "__main__":

    print("=" * 60)

    print("CyberShield AI")

    print("=" * 60)

    print("1. Scam Text")
    print("2. URL")
    print("3. Email")
    print("4. Image")

    choice = input("\nEnter choice: ")

    if choice == "1":

        text = input("\nEnter Message:\n")

        print(analyze_input(text, "text"))

    elif choice == "2":

        url = input("\nEnter URL:\n")

        print(analyze_input(url, "url"))

    elif choice == "3":

        email = input("\nEnter Email:\n")

        print(analyze_input(email, "email"))

    elif choice == "4":

        image = input("\nEnter Image Path:\n")

        print(analyze_input(image, "image"))