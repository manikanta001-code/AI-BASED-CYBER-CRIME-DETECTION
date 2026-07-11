import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


DATASET = "email_dataset.csv"


df = pd.read_csv(DATASET)


X = df["text"]

y = df["label"]



vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)



X_vector = vectorizer.fit_transform(X)



model = LinearSVC()


model.fit(
    X_vector,
    y
)



joblib.dump(
    model,
    "email_model.pkl"
)


joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)


print("Email model trained successfully")