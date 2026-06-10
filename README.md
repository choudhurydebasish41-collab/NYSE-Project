# NYSE-Project
Final project for SJS 2026 coding cohort

## Project hypothesis
 This project explores financial data from companies listed on the New York Stock Exchange (NYSE) using the Kaggle NYSE dataset. The         objective is to inspect, clean, and analyze company fundamentals to better understand relationships between key financial metrics such      as assets, revenue, debt, and profitability. Initial data processing includes identifying missing values, generating descriptive            statistics, and creating a cleaned dataset for further analysis. A central hypothesis of this project is that companies with larger         total assets tend to generate higher net income, indicating a positive relationship between company size and profitability.

## Dataset
The dataset I use is the New York Stock Exchange from Kaggle.

Fundamentals.csv contains company-level financial statement data for firms listed on the New York Stock Exchange (NYSE). The dataset includes key financial metrics such as total assets, liabilities, revenue, earnings, cash flow, and other accounting measures reported over multiple years. It provides a comprehensive view of the financial health and performance of publicly traded companies, making it useful for exploratory data analysis, financial modeling, profitability studies, and trend analysis.

## Folder Structure
- data/
  - Fundamentals.csv
  - securities.csv
- figure/
- codes/
  - inspect_nyse.py
- output/
  - clean_fundamentals_output.csv
  - fundamentals_inspection.txt
- venv/
- others/
  - NYSE_Fundamentals_Report.txt

## Data Inspection Variables and Their Purpose
- df_shape (fundamentals_df.shape)
  - Returns the overall dimensions of the dataset as (rows, columns).
  - Example: (1781, 79) means the dataset contains 1,781 records and 79 features.

- row_count (fundamentals_df.shape[0])
  - Returns the total number of rows in the dataset.
  - Helps determine the size of the dataset.

- column_count (fundamentals_df.shape[1])
  - Returns the total number of columns in the dataset.
  - Indicates how many variables or features are available for analysis.

- column_names (fundamentals_df.columns)
  - Lists all column names in the dataset.
  - Useful for understanding what financial metrics are available.

- missing_values (fundamentals_df.isna().sum())
  - Counts the number of missing values in each column.
  - Helps identify data quality issues and columns that may require cleaning.

- head_val (fundamentals_df.head())
  - Displays the first five rows of the dataset.
  - Provides a quick preview of the data structure and contents.

- tail_val (fundamentals_df.tail())
  - Displays the last five rows of the dataset.
  - Helps verify the dataset was loaded correctly and inspect the ending records.

- d_types_df (fundamentals_df.dtypes)
  - Shows the data type of each column (integer, float, string, etc.).
  - Useful for determining how each variable should be processed.

- df_desc (fundamentals_df.describe())
  - Generates descriptive statistics for numerical columns.
  - Includes count, mean, standard deviation, minimum value, maximum value, and quartiles.
  - Helps summarize the overall distribution of the data.

- ticker_count (fundamentals_df["Ticker Symbol"].value_counts())
  - Counts how many records exist for each company ticker symbol.
  - Helps understand the representation of companies within the dataset.

- fundamentals_df_clean (fundamentals_df.dropna())
  - Creates a cleaned version of the dataset by removing rows containing missing values.
  - Used to prepare the data for further analysis.

- clean_fundamentals_output.csv
  - Stores the cleaned dataset after removing missing values.
  - Can be used for future analysis and visualization.

- fundamentals_inspection.txt
  - Contains a complete inspection report including dataset dimensions, missing values, data types, summary statistics, and sample records.
  - Serves as documentation of the initial exploratory data analysis process.
