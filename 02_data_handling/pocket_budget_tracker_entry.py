import csv
from datetime import datetime

income = int(input("Enter your total monthly income or pocket money: ₹"))
category = int(input("How many categories of expenses? "))

expenses = []
names = []
percentages = []

for i in range(category):
    c = {
        "name": input(f"Enter name for category {i+1}: "),
        "amount": int(input("Enter amount: ₹"))
    }
    names.append(c["name"])
    expenses.append(c["amount"])
    p = (c["amount"] / income) * 100
    percentages.append(round(p, 2))

# --- Calculations ---
total = sum(expenses)
saving = income - total
total_per = sum(percentages)
saving_p = round(100 - total_per, 2)

print(f"\n💰 Total Expense = ₹{total}")
print(f"💵 Total Saving  = ₹{saving} ({saving_p}%)")

if saving < income * 0.2:
    print("⚠️ Warning: You’re spending over 80% of your income!")

print("\n📊 Category-wise Breakdown:")
for i in range(category):
    print(f"{names[i]} : {percentages[i]}%")

# --- Date value for this session ---
today = datetime.now().strftime("%Y-%m-%d")

# --- CSV Header ---
header = ["Category", "Amount", "Percentage", "Total Income", "Savings", "Date"]

# --- File Writing Section ---
with open('budget_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    file.seek(0, 2)          
    if file.tell() == 0:    
        writer.writerow(header)

    for i in range(category):
        writer.writerow([names[i], expenses[i], percentages[i], income, saving, today])

print("\n✅ Data saved to 'budget_data.csv' successfully!")

print("\n📂 All saved records:")
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
