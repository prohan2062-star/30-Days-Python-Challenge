
import csv
import os
from datetime import date
from collections import defaultdict

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="",
                  encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def add_expense():
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="",
              encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "date": date.today().isoformat(),
            "category": category.title(),
            "description": description,
            "amount": f"{amount:.2f}"
        })

    print("Expense added successfully!")


def read_expenses():
    with open(FILE_NAME, "r", newline="",
              encoding="utf-8") as file:
        return list(csv.DictReader(file))


def view_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"₹{float(expense['amount']):.2f}"
        )


def show_summary():
    expenses = read_expenses()

    if not expenses:
        print("No expenses to summarize.")
        return

    totals = defaultdict(float)

    for expense in expenses:
        totals[expense["category"]] += float(expense["amount"])

    grand_total = sum(totals.values())

    print("\n--- Expense Summary ---")
    print(f"Total expenses: ₹{grand_total:.2f}")

    print("\nCategory-wise expenses:")
    for category, amount in sorted(totals.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    create_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
