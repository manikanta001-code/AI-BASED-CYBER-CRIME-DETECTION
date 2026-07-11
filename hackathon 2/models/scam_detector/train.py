"""
CyberShield AI
Scam Detection Model Training

Dataset:
MENTHOS Spam Dataset

Model:
TF-IDF + Linear SVM

Output:
model.pkl
vectorizer.pkl
"""

import os
import sys

import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
)


# ---------------------------------
# Add Project Root to Python Path
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
    "menthos_train.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models",
    "scam_detector"
)


os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


# ---------------------------------
# Load Dataset
# ---------------------------------

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)


print("\nFirst rows:")
print(df.head())


print("\nDataset size:")
print(df.shape)


# ---------------------------------
# Data Cleaning
# ---------------------------------

df = df.dropna(
    subset=["text"]
)


df["text"] = df["text"].astype(str)


X = df["text"]

y = df["label"]


print("\nClass distribution:")
print(y.value_counts())


# ---------------------------------
# TF-IDF Vectorization
# ---------------------------------

print("\nCreating TF-IDF features...")


vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=100000,
    ngram_range=(1, 2)
)


X_train = vectorizer.fit_transform(X)


print(
    "Feature shape:",
    X_train.shape
)


# ---------------------------------
# Train Model
# ---------------------------------

print("\nTraining model...")


model = LinearSVC(
    class_weight="balanced"
)


model.fit(
    X_train,
    y
)


# ---------------------------------
# Evaluate Training
# ---------------------------------

prediction = model.predict(
    X_train
)


accuracy = accuracy_score(
    y,
    prediction
)


print("\nTraining Accuracy:")
print(
    round(
        accuracy * 100,
        2
    ),
    "%"
)


print("\nClassification Report:")

print(
    classification_report(
        y,
        prediction
    )
)


# ---------------------------------
# Save Model
# ---------------------------------

model_path = os.path.join(
    MODEL_DIR,
    "model.pkl"
)


vectorizer_path = os.path.join(
    MODEL_DIR,
    "vectorizer.pkl"
)


joblib.dump(
    model,
    model_path
)


joblib.dump(
    vectorizer,
    vectorizer_path
)


print("\n==============================")
print("Model training completed!")
print("==============================")


print(
    "Saved:",
    model_path
)

print(
    "Saved:",
    vectorizer_path
)