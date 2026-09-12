# ----------------------------------------------------
# Day 27: Habit Tracker & Streak Counter
# Concepts: Date Calculations, JSON Storage, Streak Maintenance, Daily Check-in
# ----------------------------------------------------

import json
import os
from datetime import datetime, date, timedelta

DATA_FILE = "habits.json"

def load_habits():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)

def calculate_streak(completed_dates):
    if not completed_dates:
        return 0

    dates = sorted([datetime.strptime(d, "%Y-%m-%d").date() for d in completed_dates])
    today = date.today()
    yesterday = today - timedelta(days=1)

    # If not completed today or yesterday, active streak is broken
    if dates[-1] not in (today, yesterday):
        return 0

    streak = 1
    for i in range(len(dates) - 1, 0, -1):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            streak += 1
        elif dates[i] == dates[i - 1]:
            continue
        else:
            break
    return streak

def add_habit(habits):
    name = input("\nEnter new habit name (e.g. 'Read 30 mins'): ").strip()
    if not name:
        print("❌ Habit name cannot be empty.")
        return

    habits.append({
        "name": name,
        "created_at": str(date.today()),
        "completed_dates": []
    })
    save_habits(habits)
    print(f"✅ Habit '{name}' created!")

def check_in_habit(habits):
    if not habits:
        print("\nNo habits created yet.")
        return

    print("\nSelect habit to check-in for TODAY:")
    for i, h in enumerate(habits, 1):
        today_str = str(date.today())
        status = "✅ (Done Today)" if today_str in h["completed_dates"] else "⏳ (Not Done)"
        print(f"{i}. {h['name']} {status}")

    try:
        idx = int(input("\nChoice: ")) - 1
        if 0 <= idx < len(habits):
            today_str = str(date.today())
            if today_str in habits[idx]["completed_dates"]:
                print("ℹ️ You already completed this habit today! Keep up the great work! 🔥")
            else:
                habits[idx]["completed_dates"].append(today_str)
                save_habits(habits)
                streak = calculate_streak(habits[idx]["completed_dates"])
                print(f"🎉 Awesome! Checked in for '{habits[idx]['name']}'. Current Streak: 🔥 {streak} day(s)!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Invalid input.")

def view_dashboard(habits):
    print("\n" + "=" * 60)
    print("🔥 DAILY HABIT TRACKER DASHBOARD 🔥".center(60))
    print("=" * 60)
    if not habits:
        print("No habits tracked yet. Add your first habit today!")
        print("=" * 60)
        return

    today_str = str(date.today())
    print(f"{'#':<3} {'Today':<8} {'Streak':<12} {'Total Days':<12} {'Habit Name'}")
    print("-" * 60)
    for i, h in enumerate(habits, 1):
        done_today = "✅" if today_str in h["completed_dates"] else "⏳"
        streak = f"🔥 {calculate_streak(h['completed_dates'])} d"
        total = f"{len(set(h['completed_dates']))} d"
        print(f"{i:<3} {done_today:<8} {streak:<12} {total:<12} {h['name']}")
    print("=" * 60)

def main():
    habits = load_habits()

    while True:
        print("\n" + "=" * 40)
        print("🌱 HABIT & STREAK TRACKER 🌱".center(40))
        print("=" * 40)
        print("1. View Habit Dashboard")
        print("2. Check-in Habit (Today)")
        print("3. Add New Habit")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()
        if choice == "1":
            view_dashboard(habits)
        elif choice == "2":
            check_in_habit(habits)
        elif choice == "3":
            add_habit(habits)
        elif choice == "4":
            print("\nStay disciplined and keep building habits! Goodbye! ✨\n")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
