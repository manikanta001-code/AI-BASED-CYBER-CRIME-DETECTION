"""
CyberShield AI
Phishing URL Detection Training

Model:
Random Forest

Input:
URL

Output:
phishing_url_model.pkl
"""

import os
import sys
import re
import joblib
import pandas as pd
import tldextract

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ---------------------------------
# Add Project Root
# ---------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

sys.path.append(PROJECT_ROOT)


from config import BASE_DIR



# ---------------------------------
# Paths
# ---------------------------------

DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "phishing_urls.csv"
)


MODEL_DIR = os.path.join(
    BASE_DIR,
    "models",
    "phishing_url"
)


os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


MODEL_PATH = os.path.join(
    MODEL_DIR,
    "phishing_url_model.pkl"
)



# ---------------------------------
# URL Feature Extraction
# ---------------------------------

def extract_features(url):

    url = str(url).lower()


    extracted = tldextract.extract(url)


    features = []


    # URL length

    features.append(
        len(url)
    )


    # Number of dots

    features.append(
        url.count(".")
    )


    # Number of hyphen

    features.append(
        url.count("-")
    )


    # Number of digits

    features.append(
        sum(
            c.isdigit()
            for c in url
        )
    )


    # Has HTTPS

    features.append(
        1 if url.startswith("https") else 0
    )


    # Has IP address

    ip_pattern = r"\d+\.\d+\.\d+\.\d+"

    features.append(
        1 if re.search(ip_pattern,url) else 0
    )


    # Suspicious words

    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "kyc",
        "free",
        "gift",
        "winner",
        "claim"
    ]


    count = 0

    for word in suspicious_words:

        if word in url:

            count += 1


    features.append(
        count
    )


    # Domain length

    features.append(
        len(extracted.domain)
    )


    return features



# ---------------------------------
# Load Dataset
# ---------------------------------

print("Loading phishing URL dataset...")


df = pd.read_csv(
    DATA_PATH
)


print(df.head())

print(
    df["label"].value_counts()
)



# ---------------------------------
# Prepare Data
# ---------------------------------

X = df["url"].apply(
    extract_features
)

y = df["label"]



# ---------------------------------
# Train Model
# ---------------------------------

print(
    "Training phishing detector..."
)


model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


model.fit(
    list(X),
    y
)



# ---------------------------------
# Evaluation
# ---------------------------------

prediction = model.predict(
    list(X)
)


accuracy = accuracy_score(
    y,
    prediction
)


print(
    "\nTraining Accuracy:",
    round(accuracy*100,2),
    "%"
)


print(
    classification_report(
        y,
        prediction
    )
)



# ---------------------------------
# Save Model
# ---------------------------------

joblib.dump(
    model,
    MODEL_PATH
)


print(
    "\nModel saved:"
)

print(
    MODEL_PATH
)