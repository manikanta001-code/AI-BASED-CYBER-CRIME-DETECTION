"""
CyberShield AI
Advanced Domain Analysis
"""

from difflib import SequenceMatcher


TRUSTED_BRANDS = {

    "google",
    "paypal",
    "amazon",
    "microsoft",
    "apple",
    "facebook",
    "instagram",
    "whatsapp",
    "github",
    "openai",
    "sbi",
    "hdfc",
    "icici",
    "axisbank"

}


def normalize(domain):

    domain = domain.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    # remove extension
    if "." in domain:
        domain = domain.split(".")[0]

    # remove symbols
    domain = domain.replace("-", "")
    domain = domain.replace("_", "")

    return domain


def analyze_domain(domain):

    cleaned = normalize(domain)

    # -----------------------
    # Real trusted domains
    # -----------------------

    if cleaned in TRUSTED_BRANDS:

        return {

            "risk_score": 0,

            "reasons": []

        }

    fake = cleaned

    # common phishing substitutions

    fake = fake.replace("0", "o")
    fake = fake.replace("1", "l")
    fake = fake.replace("3", "e")
    fake = fake.replace("5", "s")
    fake = fake.replace("7", "t")
    fake = fake.replace("@", "a")

    risk = 0

    reasons = []

    for brand in TRUSTED_BRANDS:

        # impersonation

        if fake == brand:

            risk = max(risk, 90)

            reasons.append(
                f"Fake domain impersonating '{brand}'"
            )

            continue

        # contains brand

        if brand in fake:

            risk = max(risk, 70)

            reasons.append(
                f"Trusted brand '{brand}' appears inside domain"
            )

        similarity = SequenceMatcher(
            None,
            fake,
            brand
        ).ratio()

        if similarity >= 0.80:

            risk = max(risk, 60)

            reasons.append(
                f"Domain similar to '{brand}' ({round(similarity*100)}%)"
            )

    return {

        "risk_score": risk,

        "reasons": list(set(reasons))

    }


if __name__ == "__main__":

    tests = [

        "google.com",

        "paypal.com",

        "paypa1-login.com",

        "g00gle-login.com",

        "micr0soft-security.com",

        "github.com",

        "chatgpt.com"

    ]

    for t in tests:

        print("=" * 60)

        print(t)

        print(analyze_domain(t))