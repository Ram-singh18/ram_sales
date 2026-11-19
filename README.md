# RAM SALES - Sales Data Analysis

## Project overview
This beginner-friendly data analytics project analyzes sales records using Python, Pandas and Matplotlib.

## Dataset note
`data/sales_data.csv` is a **synthetic sample/demo dataset** created for learning and demonstration. It is not real company or customer data.

## Features
- Cleans duplicate, missing and invalid records
- Calculates total sales, units sold, orders and average order value
- Identifies top-selling product and category
- Creates product, monthly trend and category charts
- Exports cleaned data and a summary report

## Requirements
- Python 3.10 or newer
- Libraries listed in `requirements.txt`

## Run on Windows
Open Command Prompt in this folder, then run:

```bash
python -m pip install -r requirements.txt
python sales_analysis.py
```

If `python` is not recognized, try:

```bash
C:\Python314\python.exe -m pip install -r requirements.txt
C:\Python314\python.exe sales_analysis.py
```

## Project structure
```text
ram_sales/
├── data/
│   ├── sales_data.csv
│   └── sales_data_cleaned.csv   (created after running)
├── outputs/
│   ├── sales_summary.csv        (created after running)
│   ├── sales_by_product.png
│   ├── monthly_sales_trend.png
│   └── sales_by_category.png
├── sales_analysis.py
├── requirements.txt
└── README.md
```

## GitHub upload
Create an empty public repository named `ram_sales`, then run these commands in Command Prompt opened inside this folder:

```bash
git init
git add .
git commit -m "Add RAM SALES data analysis project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ram_sales.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.
