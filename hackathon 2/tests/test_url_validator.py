import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, PROJECT_ROOT)


from models.phishing_url.url_validator import validate_url


urls = [

    "https://google.com",

    "https://paypal.com",

    "http://fake-bank-login.com",

    "abc",

    "ftp://example.com"

]


for url in urls:

    print("=" * 60)

    print("URL:", url)

    result = validate_url(url)

    print(result)