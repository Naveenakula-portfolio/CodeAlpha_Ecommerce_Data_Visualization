import pandas as pd
from pathlib import Path

file_path = Path("data/ecommerce_products.csv")
df = pd.read_csv(file_path)

print("DATASET VERIFICATION")
print("-" * 35)
print("Total products:", len(df))
print("Total columns:", len(df.columns))
print("Column names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())