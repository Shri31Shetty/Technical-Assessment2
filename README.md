# ETRM Data Analysis and Visualization

## Overview
This project demonstrates end-to-end data analysis and visualization workflows using multiple data formats.  
The notebook covers **data ingestion, preprocessing, and exploratory data analysis (EDA)** with meaningful insights into commodity trade data.

---

## Features
- **Data Ingestion**  
  Load data from CSV, JSON, Excel, TXT, HTML, and XML into Pandas DataFrames.

- **Data Preprocessing**  
  - Ensure consistency across datasets by verifying column names and data types.  
  - Convert `DeliveryStart` and `DeliveryEnd` columns into datetime format.  

- **Exploratory Data Analysis (EDA)**  
  - Average price per commodity.  
  - Trade volume comparisons.  
  - Distribution and trend analysis.  

- **Visualization**  
  - Heatmaps, bar charts, and trend plots to highlight insights.  

---

## Technologies Used
- **Python 3.13.3**  
- **Pandas** – data manipulation and analysis  
- **Matplotlib / Seaborn** – visualizations  
- **NumPy** – numerical computations  
- **Jupyter Notebook** – interactive environment  

---

## Project Structure
```text
Technical-Assessment2/
├── etrm_analysis.ipynb              # Main notebook with trade analysis & visualizations
├── ETRM Trade Analysis Summary.pdf  # Report with summarized findings
├── etrm_trades.csv                  # Core dataset (also in JSON, TXT, Excel, HTML, XML formats)
├── req.txt                          # Python dependencies
└── README.md                        # Project documentation

How to Run

Step 1 – Clone this repository

git clone https://github.com/Shri31Shetty/Technical-Assessment2.git
cd Technical-Assessment2


Step 2 – Install required packages

pip install -r req.txt


Step 3 – Open the Jupyter Notebook

jupyter notebook etrm_analysis.ipynb

Results & Insights

Commodities exhibit different trade behaviors (buy/sell patterns).

Gas trades are dominated by buy positions, while coal trades lean towards sell positions.

Price trends reveal market fluctuations that provide valuable insights for ETRM decision-making.
