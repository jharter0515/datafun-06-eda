import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")

# Save local copy
df.to_csv("data/penguins.csv", index=False)

print("Dataset: Palmer Penguins")
print("Rows, Columns:", df.shape)

print("\nColumns:")
for col in df.columns:
    print(f"- {col}: {df[col].dtype}")
