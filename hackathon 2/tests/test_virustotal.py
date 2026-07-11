import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, PROJECT_ROOT)

from models.phishing_url.virustotal_api import scan_url


url = input("Enter URL: ")

result = scan_url(url)

print("\n========== RESULT ==========\n")

for key, value in result.items():
    print(f"{key}: {value}")