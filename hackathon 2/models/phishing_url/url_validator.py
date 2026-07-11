"""
CyberShield AI
URL Validator
"""

from urllib.parse import urlparse


def validate_url(url):

    try:

        parsed = urlparse(url)

        valid = (
            parsed.scheme in ("http", "https")
            and parsed.netloc != ""
        )

        return {

            "valid": valid,

            "domain": parsed.netloc,

            "scheme": parsed.scheme,

            "path": parsed.path

        }

    except Exception as e:

        return {

            "valid": False,

            "domain": "",

            "scheme": "",

            "path": "",

            "error": str(e)

        }