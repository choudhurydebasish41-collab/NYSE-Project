from pathlib import Path
import pandas as pd

project = Path(__file__).resolve().parents[1]

data_folder = project / "data"
results_folder = project / "results"
figures_folder = project / "figures"

results_folder.mkdir(exist_ok=True)
figures_folder.mkdir(exist_ok=True)

input_csv = data_folder / "fundamentals.csv"

fundamentals_df = pd.read_csv(str(input_csv))

df_shape = fundamentals_df.shape
row_count = fundamentals_df.shape[0]
column_count = fundamentals_df.shape[1]
column_names = fundamentals_df.columns
missing_values = fundamentals_df.isna().sum()

head_val = fundamentals_df.head()
tail_val = fundamentals_df.tail()
d_types_df = fundamentals_df.dtypes
df_desc = fundamentals_df.describe()

if "Ticker Symbol" in fundamentals_df.columns:
    ticker_count = fundamentals_df["Ticker Symbol"].value_counts()
else:
    ticker_count = "No ticker column found."

fundamentals_df_clean = fundamentals_df.dropna()

output_csv = results_folder / "clean_fundamentals_output.csv"
fundamentals_df_clean.to_csv(output_csv, index=False)

review_output = results_folder / "fundamentals_inspection.txt"

with open(review_output, "w") as file:
    file.write(f"Shape of the dataframe: {df_shape}\n")
    file.write(f"# of rows: {row_count}\n")
    file.write(f"# of columns: {column_count}\n\n")

    file.write("Column names:\n")
    for column in column_names:
        file.write(f"- {column}\n")

    file.write("\nMissing values:\n")
    file.write(f"{missing_values}\n\n")

    file.write("Ticker count for each company:\n")
    file.write(f"{ticker_count}\n\n")

    file.write("Top 5 rows:\n")
    file.write(f"{head_val}\n\n")

    file.write("Bottom 5 rows:\n")
    file.write(f"{tail_val}\n\n")

    file.write("Datatypes of each column:\n")
    file.write(f"{d_types_df}\n\n")

    file.write("Numeric summary:\n")
    file.write(f"{df_desc}\n")

print("Fundamentals inspection complete.")
print(f"Clean CSV saved to: {output_csv}")
print(f"Inspection text saved to: {review_output}")