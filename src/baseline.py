import pandas as pd

# Load dataset
df1 = pd.read_csv('C:\\Users\\ASUS\\Downloads\\hedging_dataset_v0.1.csv')
print(df1.head())

# Count labels
counts = df1['label'].value_counts()
print(counts)

# Load hedging cues
df2 = pd.read_json('C:\\Users\\ASUS\\Downloads\\hedging_cues (1).json')

# Convert cues column to list
hedging_cues = df2[0].str.lower().tolist()

# User input
statement = input("Enter your statement: ").lower()

# Check for hedging
while True:
    statement = input("\nEnter a statement (or type 'quit' to exit): ")

    if statement.lower() == "quit":
        break

    found = False

    for cue in hedging_cues:
        if cue in statement.lower():
            found = True
            print(f"Hedging cue detected: '{cue}'")

    if found:
        print("The statement consists of hedging terms.")
    else:
        print("The statement does not consist of hedging terms.")
