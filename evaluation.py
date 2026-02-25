import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json

# --------------------------------
# 1. Load Dataset
# --------------------------------
df = pd.read_csv("C:\\Users\\ASUS\\Pragmatics-Aware-Statement-Analyzer\\hedging_dataset_v0.1 (1).csv", encoding='cp1252')

# --------------------------------
# 2. Load Hedging Cues
# --------------------------------

with open("hedging_cues.json", "r") as f:
    hedging_cues = json.load(f)

# Ensure lowercase
hedging_cues = [cue.lower() for cue in hedging_cues]


# --------------------------------
# 3. Baseline Rule-Based Predictor
# --------------------------------
# If a sentence contains a hedging term → predict hedge (1)
# Otherwise → predict non-hedge (0)

def predict_hedge(text):
    text = text.lower()
    for cue in hedging_cues:
        if cue in text:
            return 1
    return 0

df["prediction"] = df["text"].apply(predict_hedge)

# --------------------------------
# 4. Evaluation Metrics
# --------------------------------
y_true = df["label"]
y_pred = df["prediction"]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Baseline Evaluation Results")
print("----------------------------")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# --------------------------------
# 5. Identify False Positives
# --------------------------------
# Predicted hedge but actually not hedge

false_positives = df[(df["prediction"] == 1) & (df["label"] == 0)]

print("\nFalse Positives (Top 5)")
print(false_positives.head(5)["text"])

# --------------------------------
# 6. Identify False Negatives
# --------------------------------
# Actual hedge but model missed it

false_negatives = df[(df["prediction"] == 0) & (df["label"] == 1)]

print("\nFalse Negatives (Top 5)")
print(false_negatives.head(5)["text"])

# --------------------------------
# 7. Save Errors for Analysis
# --------------------------------
false_positives.to_csv("false_positives.csv", index=False)
false_negatives.to_csv("false_negatives.csv", index=False)

print("\nSaved error files:")
print("false_positives.csv")
print("false_negatives.csv")
