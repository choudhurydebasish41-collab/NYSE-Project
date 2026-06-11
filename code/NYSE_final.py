from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project = Path(__file__).resolve().parents[1]

data_folder = project / "data"
results_folder = project / "results"
figures_folder = project / "figures"

results_folder.mkdir(exist_ok=True)
figures_folder.mkdir(exist_ok=True)

input_csv = data_folder / "fundamentals.csv"

df = pd.read_csv(input_csv)

# -----------------------------
# 1. INSPECTION
# -----------------------------

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)

ticker_counts = df["Ticker Symbol"].value_counts()
missing_values = df.isna().sum()

# -----------------------------
# 2. SELECTION AND INDEXING
# -----------------------------

selected_columns = [
    "Ticker Symbol",
    "For Year",
    "Total Liabilities",
    "Total Equity",
    "Long-Term Debt",
    "Net Income",
    "Operating Income",
    "Profit Margin",
    "Total Revenue"
]

df_selected = df[selected_columns]

first_row = df_selected.iloc[0]
first_five_rows = df_selected.iloc[0:5]
specific_value = df_selected.loc[0, "Ticker Symbol"]
sample_rows = df_selected.sample(10, random_state=42)

# -----------------------------
# 3. CLEANING
# -----------------------------

df_clean = df_selected.copy()

df_clean = df_clean.drop_duplicates()

df_clean = df_clean.dropna(
    subset=[
        "Total Liabilities",
        "Total Equity",
        "Net Income",
        "Long-Term Debt",
        "For Year"
    ]
)

df_clean["For Year"] = df_clean["For Year"].astype(int)

df_clean = df_clean[df_clean["Total Equity"] != 0]
df_clean = df_clean[df_clean["Total Revenue"] != 0]

# -----------------------------
# 4. TRANSFORMATION
# -----------------------------

df_clean = df_clean.rename(columns={
    "Ticker Symbol": "Ticker",
    "For Year": "Year"
})

df_clean["Debt_to_Equity"] = (
    df_clean["Total Liabilities"] / df_clean["Total Equity"]
)

df_clean["Debt_to_Revenue"] = (
    df_clean["Long-Term Debt"] / df_clean["Total Revenue"]
)

df_clean = df_clean.replace([float("inf"), -float("inf")], pd.NA)
df_clean = df_clean.dropna(subset=["Debt_to_Equity", "Debt_to_Revenue"])

df_clean = df_clean.sort_values("Debt_to_Equity", ascending=False)

df_clean["Debt_Group"] = pd.qcut(
    df_clean["Debt_to_Equity"],
    3,
    labels=["Low Debt", "Medium Debt", "High Debt"]
)

grouped_profit = df_clean.groupby("Debt_Group")["Net Income"].mean()

# -----------------------------
# 5. ANALYSIS
# -----------------------------

debt_profit_corr = df_clean["Debt_to_Equity"].corr(df_clean["Net Income"])
debt_margin_corr = df_clean["Debt_to_Equity"].corr(df_clean["Profit Margin"])

# -----------------------------
# 6. GRAPHS
# -----------------------------

# plt.figure(figsize=(8, 6))
# plt.scatter(df_clean["Debt_to_Equity"], df_clean["Net Income"])
# plt.xlabel("Debt-to-Equity Ratio")
# plt.ylabel("Net Income")
# plt.title("Debt-to-Equity Ratio vs Net Income")
# plt.tight_layout()
# plt.savefig(figures_folder / "debt_to_equity_vs_net_income.png")
# plt.close()

plt.figure(figsize=(8, 6))
grouped_profit.plot(kind="bar")
plt.xlabel("Debt Group")
plt.ylabel("Average Net Income")
plt.title("Average Net Income by Debt Group")
plt.tight_layout()
plt.savefig(figures_folder / "average_net_income_by_debt_group.png")
plt.close()

# plt.figure(figsize=(8, 6))
# plt.scatter(df_clean["Debt_to_Equity"], df_clean["Profit Margin"])
# plt.xlabel("Debt-to-Equity Ratio")
# plt.ylabel("Profit Margin")
# plt.title("Debt-to-Equity Ratio vs Profit Margin")
# plt.tight_layout()
# plt.savefig(figures_folder / "debt_to_equity_vs_profit_margin.png")
# plt.close()

plt.figure(figsize=(8, 6))

df_clean.boxplot(
    column="Net Income",
    by="Debt_Group"
)

plt.title("Net Income Distribution by Debt Group")
plt.suptitle("")
plt.xlabel("Debt Group")
plt.ylabel("Net Income")

plt.tight_layout()
plt.savefig(
    figures_folder / "net_income_boxplot_by_debt_group.png"
)
plt.close()

# -----------------------------
# 7. SAVE OUTPUTS
# -----------------------------

df_clean.to_csv(results_folder / "debt_profit_cleaned_data.csv", index=False)

with open(results_folder / "debt_profit_analysis.txt", "w") as file:
    file.write("Research Question:\n")
    file.write("Is there a relationship between a company's debt level and its profit generation?\n\n")

    file.write("Dataset Inspection:\n")
    file.write(f"Shape: {df.shape}\n")
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n\n")

    file.write("Missing Values:\n")
    file.write(f"{missing_values}\n\n")

    file.write("Ticker Counts:\n")
    file.write(f"{ticker_counts}\n\n")

    file.write("Selected Columns:\n")
    for col in selected_columns:
        file.write(f"- {col}\n")

    file.write("\nCorrelation Results:\n")
    file.write(f"Debt-to-Equity vs Net Income correlation: {debt_profit_corr}\n")
    file.write(f"Debt-to-Equity vs Profit Margin correlation: {debt_margin_corr}\n\n")

    file.write("Average Net Income by Debt Group:\n")
    file.write(f"{grouped_profit}\n\n")

    file.write("Conclusion Draft:\n")
    file.write(
        "This analysis compares company debt levels with profit generation. "
        "Debt-to-equity ratio was used as the main debt measurement, while net income "
        "and profit margin were used as profitability measurements. "
        "The correlation values and debt-group averages help determine whether companies "
        "with higher debt tend to generate higher profits. If the correlation is weak, "
        "then debt level alone does not strongly explain profitability."
    )

print("Analysis complete.")