import pandas as pd

df = pd.read_csv("dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("Shape after cleaning:", df.shape)

# Save cleaned dataset
df.to_csv("clean_dataset.csv", index=False)

print("Dataset Cleaned Successfully!")


import matplotlib.pyplot as plt

df["Career"].value_counts().plot(kind="bar", figsize=(12,6))

plt.title("Career Distribution")

plt.xlabel("Career")

plt.ylabel("Students")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()