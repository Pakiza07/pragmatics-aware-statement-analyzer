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
