BLACKLIST_DOMAINS = [

    "paypa1-login.com",
    "fakebank.com",
    "secure-update-login.com"

]


def check_reputation(domain):

    risk = 0
    reasons = []


    if domain in BLACKLIST_DOMAINS:

        risk += 60

        reasons.append(
            "Domain found in blacklist"
        )


    return {

        "reputation_risk":risk,

        "reasons":reasons

    }