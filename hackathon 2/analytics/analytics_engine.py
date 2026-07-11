import json
import os
import pandas as pd


def load_alerts():

    file_path = os.path.join(
        "alerts",
        "quarantine.json"
    )

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        data = json.load(file)

    return data



def create_dataframe():

    alerts = load_alerts()

    if len(alerts) == 0:
        return pd.DataFrame()

    df = pd.DataFrame(alerts)

    return df



def threat_statistics():

    df = create_dataframe()

    if df.empty:
        return {}

    stats = {

        "total_threats": len(df),

        "threat_types":
            df["threat_type"]
            .value_counts()
            .to_dict(),

        "actions":
            df["action"]
            .value_counts()
            .to_dict()
    }

    return stats



def risk_distribution():

    df = create_dataframe()

    if df.empty:
        return {}

    bins = [
        0,
        20,
        40,
        60,
        80,
        100
    ]

    labels = [
        "0-20",
        "20-40",
        "40-60",
        "60-80",
        "80-100"
    ]

    df["risk_range"] = pd.cut(
        df["risk_score"],
        bins=bins,
        labels=labels
    )

    return (
        df["risk_range"]
        .value_counts()
        .to_dict()
    )