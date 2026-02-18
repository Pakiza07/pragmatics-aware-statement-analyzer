import pandas as pd
import string


# ---------- PREPROCESSING FUNCTION ----------
def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove extra whitespace
    text = " ".join(text.split())

    # 4. Tokenization (simple split)
    tokens = text.split()

    return tokens


# ---------- LOAD DATASET ----------
df = pd.read_csv('C:\\Users\\ASUS\\OneDrive\\Desktop\\records.csv', encoding='cp1252')



# ---------- TEST ON FIRST 5 STATEMENTS ----------
for i, row in df.head(5).iterrows():
    original = row["Text"]
    processed = preprocess_text(original)

    print("Original:", original)
    print("Processed:", processed)
    print("-" * 50)

# -----------------------------
# Load hedging cues from JSON
# -----------------------------
with open("hedging_cues.json", "r") as f:
    hedging_cues = json.load(f)

# Ensure lowercase
hedging_cues = [cue.lower() for cue in hedging_cues]

# -----------------------------
# Separate single vs phrase cues
# -----------------------------
single_word_cues = [cue for cue in hedging_cues if " " not in cue]
phrase_cues = [cue for cue in hedging_cues if " " in cue]


# -----------------------------
# Detection function
# -----------------------------
def detect_hedging(Text):
    tokens = preprocess_text(Text)
    processed_text = " ".join(tokens)

    # check single-word cues
    for token in tokens:
        if token in single_word_cues:
            return 1

    # check phrase cues
    for phrase in phrase_cues:
        if phrase in processed_text:
            return 1

    return 0


# -----------------------------
# Apply detection to dataset
# -----------------------------
df["prediction"] = df["Text"].apply(detect_hedging)


# -----------------------------
# Basic evaluation
# -----------------------------
df["error"] = df["Label"] != df["prediction"]

false_positives = df[(df["prediction"] == 1) & (df["Label"] == 0)]
false_negatives = df[(df["prediction"] == 0) & (df["Label"] == 1)]

print("Total samples:", len(df))
print("False Positives:", len(false_positives))
print("False Negatives:", len(false_negatives))


# Save error analysis
false_positives.to_csv("false_positives.csv", index=False)
false_negatives.to_csv("false_negatives.csv", index=False)
