import requests

from modules.image_detector.api.config import API_USER, API_SECRET


def analyze_ai_image(image_path):

    url = "https://api.sightengine.com/1.0/check.json"

    with open(image_path, "rb") as img:

        response = requests.post(
            url,
            files={"media": img},
            data={
                "models": "genai",
                "api_user": API_USER,
                "api_secret": API_SECRET,
            },
        )

    return response.json()