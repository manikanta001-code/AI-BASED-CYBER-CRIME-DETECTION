import pandas as pd

print("=" * 60)
print("SMS DATASET")
print("=" * 60)

# Change the filename if yours is different
sms = pd.read_csv("datasets/SMSSpamCollection", sep="\t", header=None)

print(sms.head())
print()
print("Columns:", sms.columns)

print("\n" + "=" * 60)
print("EMAIL DATASET")
print("=" * 60)

# Change the filename if yours is different
email = pd.read_csv("datasets/email_spam.csv")

print(email.head())
print()
print("Columns:", email.columns)