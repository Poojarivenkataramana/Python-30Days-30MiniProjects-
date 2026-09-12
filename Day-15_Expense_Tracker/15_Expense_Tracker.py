# ----------------------------------------------------
# Day 15: Daily Expense Tracker
# Concepts: File Persistence (JSON), Datetime, Aggregations, Categorization
# ----------------------------------------------------

import json
import os
from datetime import datetime

EXPENSE_FILE = "expenses.json"

CATEGORIES = ["Food & Dining", "Transport", "Shopping", "Bills & Utilities", "Entertainment", "Health", "Other"]

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        try:
            with open(EXPENSE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    print("\n--- ➕ Add New Expense ---")
    try:
        amount = float(input("Enter amount spent: "))
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return

    print("\nSelect Category:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")

    try:
        cat_choice = int(input(f"Choice (1-{len(CATEGORIES)}): "))
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            category = "Other"
    except ValueError:
        category = "Other"

    desc = input("Enter description / note: ").strip()
    if not desc:
        desc = "No description"

    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    new_item = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": desc,
        "date": date_str
    }
    expenses.append(new_item)
    save_expenses(expenses)
    print(f"✅ Expense of ₹/{amount:.2f} logged under '{category}'!")

def view_expenses(expenses):
    print("\n" + "=" * 65)
    print("📋 EXPENSE HISTORY 📋".center(65))
    print("=" * 65)
    if not expenses:
        print("No expenses recorded yet! 💸")
        print("=" * 65)
        return

    print(f"{'ID':<4} {'Date':<18} {'Category':<18} {'Amount':<10} {'Note'}")
    print("-" * 65)
    for exp in expenses:
        print(f"{exp['id']:<4} {exp['date']:<18} {exp['category']:<18} {exp['amount']:>8.2f}  {exp['description']}")
    print("=" * 65)

def category_summary(expenses):
    if not expenses:
        print("\nNo expense data available for summary.")
        return

    totals = {}
    total_spent = 0.0

    for exp in expenses:
        cat = exp["category"]
        amt = exp["amount"]
        totals[cat] = totals.get(cat, 0.0) + amt
        total_spent += amt

    print("\n" + "=" * 50)
    print("📊 EXPENSE CATEGORY BREAKDOWN 📊".center(50))
    print("=" * 50)
    print(f"{'Category':<22} {'Amount':<12} {'Percentage'}")
    print("-" * 50)
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total_spent) * 100
        print(f"{cat:<22} {amt:>10.2f}   {pct:>6.1f}%")
    print("-" * 50)
    print(f"{'TOTAL SPENT':<22} {total_spent:>10.2f}   100.0%")
    print("=" * 50)

def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 40)
        print("💰 PERSONAL EXPENSE TRACKER 💰".center(40))
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Breakdown")
        print("4. Clear All Expenses")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            category_summary(expenses)
        elif choice == "4":
            confirm = input("⚠️ Are you sure you want to delete all records? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                expenses = []
                save_expenses(expenses)
                print("🗑️ All expenses cleared.")
        elif choice == "5":
            print("\nStay financially healthy! Goodbye! 👋\n")
            break
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
