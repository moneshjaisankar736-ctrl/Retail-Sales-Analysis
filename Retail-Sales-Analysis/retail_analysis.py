import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("sales_data.csv")

print("\n===== RETAIL SALES ANALYSIS =====\n")

# Total Sales
print("Total Sales:", df["Sales"].sum())

# Total Profit
print("Total Profit:", df["Profit"].sum())

# Sales by Category
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

# Sales by Region
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

# Top 5 Products
print("\nTop 5 Products:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5))

# -----------------------------
# Category Chart
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_chart.png")

# -----------------------------
# Top 10 Products Chart
# -----------------------------
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")

print("\nCategory chart saved as category_chart.png")
print("Top products chart saved as sales_chart.png")