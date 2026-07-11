"""
CyberShield AI
Alert History
"""

import json
import os
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ALERT_FILE = os.path.join(
    BASE_DIR,
    "quarantine.json"
)


def load_alerts():

    if not os.path.exists(ALERT_FILE):

        return pd.DataFrame()

    try:

        with open(ALERT_FILE, "r") as f:

            data = json.load(f)

        return pd.DataFrame(data)

    except Exception:

        return pd.DataFrame()


def get_statistics(df):

    if df.empty:

        return {

            "total": 0,

            "blocked": 0,

            "review": 0,

            "allowed": 0

        }

    blocked = len(

        df[df["action"] == "BLOCK"]

    )

    review = len(

        df[df["action"] == "REVIEW"]

    )

    allowed = len(

        df[df["action"] == "ALLOW"]

    )

    return {

        "total": len(df),

        "blocked": blocked,

        "review": review,

        "allowed": allowed

    }


if __name__ == "__main__":

    df = load_alerts()

    print(df)

    print()

    print(get_statistics(df))