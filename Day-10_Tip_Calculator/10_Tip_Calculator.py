# ----------------------------------------------------
# Day 10: Tip & Split Bill Calculator
# Concepts: Floating point arithmetic, String formatting, Conditionals
# ----------------------------------------------------

def main():
    print("=" * 45)
    print("💵 TIP & SPLIT BILL CALCULATOR 💵".center(45))
    print("=" * 45)

    try:
        bill = float(input("Enter total bill amount ($ / ₹): "))
        if bill <= 0:
            print("❌ Bill amount must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a numeric bill amount.")
        return

    print("\nTip Options:")
    print("1. 10% (Good)")
    print("2. 15% (Great)")
    print("3. 20% (Excellent)")
    print("4. Custom %")

    tip_choice = input("\nSelect tip option (1-4): ").strip()

    if tip_choice == "1":
        tip_percent = 10.0
    elif tip_choice == "2":
        tip_percent = 15.0
    elif tip_choice == "3":
        tip_percent = 20.0
    elif tip_choice == "4":
        try:
            tip_percent = float(input("Enter custom tip percentage (%): "))
            if tip_percent < 0:
                print("❌ Tip percentage cannot be negative.")
                return
        except ValueError:
            print("❌ Invalid percentage!")
            return
    else:
        print("❌ Invalid selection, defaulting to 15%.")
        tip_percent = 15.0

    try:
        people = int(input("\nEnter number of people to split the bill: "))
        if people <= 0:
            print("❌ Number of people must be at least 1.")
            return
    except ValueError:
        print("❌ Invalid number of people!")
        return

    # Calculations
    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    per_person = total_bill / people

    # Receipt display
    print("\n" + "-" * 45)
    print("🧾 FINAL BILL RECEIPT 🧾".center(45))
    print("-" * 45)
    print(f"{'Original Bill Amount':<25}: {bill:>10.2f}")
    print(f"{f'Tip Percentage ({tip_percent}%)':<25}: {tip_amount:>10.2f}")
    print(f"{'Total Bill with Tip':<25}: {total_bill:>10.2f}")
    print(f"{'Split Count':<25}: {people:>10} person(s)")
    print("-" * 45)
    print(f"{'💰 Amount Per Person':<25}: {per_person:>10.2f}")
    print("=" * 45)

if __name__ == "__main__":
    main()
