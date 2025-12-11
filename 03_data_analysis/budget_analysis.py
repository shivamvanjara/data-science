import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = 'budget_data.csv'

if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"'{CSV_FILE}' not found. Run Day 3 to create it or place the file here.")

df = pd.read_csv(CSV_FILE)

numeric_cols = ['Amount', 'Percentage', 'Total Income', 'Savings']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Category', 'Amount'])

print("== Top Rows ==")
print(df.head())
print("\n== Summary ==")
print(df.describe(include='all'))

summary = df.groupby('Category', as_index=False).agg({
    'Amount': 'sum',
    'Percentage': 'mean',
    'Total Income': 'mean',
    'Savings': 'mean'
})

summary['Pct_of_total'] = (summary['Amount'] / summary['Amount'].sum()) * 100
summary = summary.sort_values(by='Amount', ascending=False).reset_index(drop=True)

print("\n== Category Summary ==")
print(summary[['Category', 'Amount', 'Pct_of_total']])

total_spent = summary['Amount'].sum()
avg_per_category = summary['Amount'].mean()
highest = summary.iloc[0]  #
print(f"\nTotal Spent: ₹{total_spent:.2f}")
print(f"Average Spending per Category: ₹{avg_per_category:.2f}")
print(f"Highest Spending Category: {highest['Category']} (₹{highest['Amount']:.2f})")


plt.figure(figsize=(8, 5))
plt.bar(summary['Category'], summary['Amount'])
plt.title('Total Expense by Category')
plt.xlabel('Category')
plt.ylabel('Amount (₹)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 7))
plt.pie(summary['Pct_of_total'], labels=summary['Category'], autopct='%1.1f%%', startangle=90)
plt.title('Category-wise Expense Percentage')
plt.axis('equal')
plt.show()

OUTPUT = 'budget_summary.csv'
summary.to_csv(OUTPUT, index=False)
print(f"\nSummary saved to '{OUTPUT}'")
