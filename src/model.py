import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

import numpy as np

# --------------------------------------
# 1. Load dataset
# --------------------------------------
df = pd.read_csv("C:\\Users\\ASUS\\Pragmatics-Aware-Statement-Analyzer\\hedging_dataset_v0.1 (1).csv", encoding='cp1252')

texts = df["text"]
labels = df["label"]

# --------------------------------------
# 2. Load saved TF-IDF vectorizer
# --------------------------------------
vectorizer = joblib.load("C:\\Users\\ASUS\\Pragmatics-Aware-Statement-Analyzer\\venv\\tfidf_vectorizer.pkl")

# Convert text → features
X = vectorizer.transform(texts)
y = labels

# --------------------------------------
# 3. Train/Test Split
# --------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# --------------------------------------
# 4. Train Model
# --------------------------------------
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel training complete.")

# --------------------------------------
# 5. Generate Predictions
# --------------------------------------
y_pred = model.predict(X_test)

# --------------------------------------
# 6. Evaluation Metrics
# --------------------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n=== ML Model Performance ===")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# --------------------------------------
# 7. Save Model
# --------------------------------------
joblib.dump(model, "hedge_classifier.pkl")

print("\nModel saved as hedge_classifier.pkl")

# --------------------------------------
# 8. Save Predictions
# --------------------------------------
results = pd.DataFrame({
    "text": df.loc[y_test.index, "text"],
    "true_label": y_test,
    "predicted_label": y_pred
})

results.to_csv("ml_predictions.csv", index=False)

print("Predictions saved to ml_predictions.csv")

# --------------------------------------
# 9. Create Confusion Matrix
# --------------------------------------
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.title("Confusion Matrix — Hedge Classifier")
plt.savefig("confusion_matrix.png")
plt.close()

# --------------------------------------
# 10. Feature Importance Analysis
# --------------------------------------
feature_names = vectorizer.get_feature_names_out()

coefficients = model.coef_[0]

top_positive = np.argsort(coefficients)[-20:]
top_negative = np.argsort(coefficients)[:20]

print("Top Hedge Indicators:")
print(feature_names[top_positive])

print("\nTop Non-Hedge Indicators:")
print(feature_names[top_negative])


# --------------------------------------
# 11. Highlighting Hedge Terms in Text
# --------------------------------------
def highlight_hedges(text, hedge_terms):
    for term in hedge_terms:
        text = text.replace(term, f"[{term.upper()}]")
    return text

