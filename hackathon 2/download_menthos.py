import pandas as pd

df = pd.read_csv("datasets/menthos_train.csv")

print(df.head())

print(df.columns)

print(df["label"].value_counts())