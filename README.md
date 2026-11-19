# RAM SALES - Sales Data Analysis

## Project Overview

RAM SALES is a beginner-friendly Data Analytics project that analyzes sales records using Python, Pandas, NumPy and Matplotlib.

## Dataset Note

`data/sales_data.csv` is a synthetic sample/demo dataset created for learning and demonstration. It does not contain real company or customer data.

## Features

- Removes duplicate and missing records.
- Cleans invalid sales records.
- Calculates total sales and units sold.
- Calculates total orders and average order value.
- Identifies the top-selling product and category.
- Generates monthly sales trend visualization.
- Creates product-wise and category-wise sales charts.
- Exports cleaned data and sales summary reports.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## Requirements

- Python 3.10 or newer
- Libraries listed in `requirements.txt`

## How to Run the Project

### Step 1: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 2: Run the Project

```bash
python sales_analysis.py
```

### Step 3: View Results

After successful execution, check the `outputs` folder for generated charts and reports.

## Project Structure

```text
ram_sales/
├── data/
│   ├── sales_data.csv
│   └── sales_data_cleaned.csv
├── outputs/
│   ├── sales_summary.csv
│   ├── sales_by_product.png
│   ├── monthly_sales_trend.png
│   └── sales_by_category.png
├── sales_analysis.py
├── requirements.txt
└── README.md
```

## Author

Ramsingh Thakur

## GitHub Repository

https://github.com/Ram-singh18/ram_sales
