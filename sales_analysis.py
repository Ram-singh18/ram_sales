"""
RAM SALES - Sales Data Analysis
A beginner-friendly Python, Pandas and Matplotlib project.
Dataset: sample/demo data generated for this project.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    data = pd.read_csv(DATA_FILE)
    print("\\n========== RAM SALES: SALES DATA ANALYSIS ==========")
    print(f"Original rows: {len(data)}")

    # Data cleaning
    data = data.drop_duplicates(subset=["Order_ID"])
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for col in ["Quantity", "Unit_Price", "Sales"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna(subset=["Date", "Product", "Category", "Quantity", "Unit_Price"])
    data = data[data["Quantity"] > 0]
    data["Sales"] = data["Quantity"] * data["Unit_Price"]
    data.to_csv(BASE_DIR / "data" / "sales_data_cleaned.csv", index=False)

    # Key metrics
    total_sales = data["Sales"].sum()
    total_units = data["Quantity"].sum()
    total_orders = data["Order_ID"].nunique()
    average_order_value = total_sales / total_orders if total_orders else 0
    top_product = data.groupby("Product")["Sales"].sum().idxmax()
    top_category = data.groupby("Category")["Sales"].sum().idxmax()

    print(f"Clean rows: {len(data)}")
    print(f"Total Sales: Rs. {total_sales:,.2f}")
    print(f"Total Units Sold: {total_units:,.0f}")
    print(f"Total Orders: {total_orders}")
    print(f"Average Order Value: Rs. {average_order_value:,.2f}")
    print(f"Top Product: {top_product}")
    print(f"Top Category: {top_category}")

    # Save summary
    summary = pd.DataFrame({
        "Metric": ["Total Sales", "Total Units Sold", "Total Orders",
                   "Average Order Value", "Top Product", "Top Category"],
        "Value": [round(total_sales, 2), int(total_units), int(total_orders),
                  round(average_order_value, 2), top_product, top_category]
    })
    summary.to_csv(OUTPUT_DIR / "sales_summary.csv", index=False)

    # Chart 1: sales by product
    product_sales = data.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    product_sales.plot(kind="bar")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales (Rs.)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_product.png", dpi=150)
    plt.close()

    # Chart 2: monthly sales
    monthly_sales = data.set_index("Date").resample("MS")["Sales"].sum()
    plt.figure(figsize=(9, 5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (Rs.)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=150)
    plt.close()

    # Chart 3: sales by category
    category_sales = data.groupby("Category")["Sales"].sum()
    plt.figure(figsize=(7, 5))
    category_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Sales Share by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
    plt.close()

    print("\\nProject completed successfully.")
    print(f"Cleaned data and reports saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
