def check_email_security(domain):

    score = 0
    reasons = []


    # Simulation
    # Later connect DNS APIs


    if domain:

        score += 10

        reasons.append(
            "Security records checked"
        )


    return {

        "security_score":score,

        "reasons":reasons

    }