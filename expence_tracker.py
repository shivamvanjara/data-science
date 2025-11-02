# Daily Expense Tracker (Do-While Version)
# Author: Shivam Vanjara

expenses = []  # list to store expense amounts

def show_summary():
    """Display total and average expenses."""
    if expenses:
        total = sum(expenses)
        avg = total / len(expenses)
        print(f"\n💵 Total Expense: ₹{total:.2f}")
        print(f"📊 Average Expense per Transaction: ₹{avg:.2f}\n")
    else:
        print("\n⚠️ No expenses recorded yet!\n")

# simulate do-while loop
while True:
    print("\n===== Daily Expense Tracker =====")
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. View Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter expense amount: ₹"))
        expenses.append(amount)
        print(f"✅ Added ₹{amount:.2f}")
        show_summary()

    elif choice == '2':
        if not expenses:
            print("⚠️ No expenses to update!")
        else:
            for i, val in enumerate(expenses, start=1):
                print(f"{i}. ₹{val:.2f}")
            index = int(input("Enter number to update: ")) - 1
            if 0 <= index < len(expenses):
                new_amount = float(input("Enter new amount: ₹"))
                expenses[index] = new_amount
                print("✅ Expense updated successfully!")
            else:
                print("❌ Invalid index.")
            show_summary()

    elif choice == '3':
        if not expenses:
            print("⚠️ No expenses to delete!")
        else:
            for i, val in enumerate(expenses, start=1):
                print(f"{i}. ₹{val:.2f}")
            index = int(input("Enter number to delete: ")) - 1
            if 0 <= index < len(expenses):
                removed = expenses.pop(index)
                print(f"🗑️ Deleted ₹{removed:.2f}")
            else:
                print("❌ Invalid index.")
            show_summary()

    elif choice == '4':
        show_summary()

    elif choice == '5':
        print("👋 Exiting Daily Expense Tracker...")
        break

    else:
        print("❌ Invalid choice. Please try again.")

    # this acts like a do-while continuation prompt
    again = input("Do you want to perform another operation? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Goodbye! Have a nice day.")
        break
