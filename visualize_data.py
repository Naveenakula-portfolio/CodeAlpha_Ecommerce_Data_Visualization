import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
df = pd.read_csv("data/ecommerce_products.csv")

# Create charts output folder
output_dir = Path("outputs/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Product price distribution
df["price_value"] = pd.to_numeric(
    df["price_value"], errors="coerce"
)

plt.figure(figsize=(8, 5))
df["price_value"].dropna().hist(bins=10, edgecolor="black")
plt.title("Distribution of E-commerce Product Prices")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(output_dir / "price_distribution.png", dpi=300)
plt.show()

# 2. Product ratings
rating_counts = df["rating"].value_counts()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(output_dir / "rating_distribution.png", dpi=300)
plt.show()

print("Charts saved successfully in:", output_dir.resolve())

# 3. Product categories
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")
plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(output_dir / "category_distribution.png", dpi=300)
plt.show()

print("All charts generated successfully!")