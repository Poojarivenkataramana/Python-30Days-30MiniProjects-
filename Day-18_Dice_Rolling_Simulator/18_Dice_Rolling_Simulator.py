# ----------------------------------------------------
# Day 18: Dice Rolling Simulator & Statistical Analyzer
# Concepts: Random module, ASCII visuals, Frequency distribution, Simulation
# ----------------------------------------------------

import random
from collections import Counter

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

def display_dice(rolls):
    for row in range(5):
        line = "  ".join(DICE_ART[val][row] for val in rolls)
        print(line)

def interactive_roll():
    while True:
        try:
            num = input("\nHow many dice would you like to roll? (1-5, or 'q' to quit): ").strip()
            if num.lower() in ("q", "quit"):
                break
            num_dice = int(num)
            if not (1 <= num_dice <= 5):
                print("❌ Please choose between 1 and 5 dice.")
                continue
        except ValueError:
            print("❌ Invalid integer input.")
            continue

        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)

        print(f"\n🎲 Rolling {num_dice} dice...\n")
        display_dice(results)
        print(f"\nRoll Values : {results}")
        print(f"Total Sum   : {total}")
        print("-" * 45)

def run_simulation():
    print("\n--- 📊 Statistical Roll Simulator ---")
    try:
        n = int(input("Enter number of rolls to simulate (e.g. 10000): "))
        if n <= 0:
            print("❌ Must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return

    counts = Counter(random.randint(1, 6) for _ in range(n))

    print("\n" + "=" * 50)
    print(f"SIMULATION RESULTS ({n:,} ROLLS)".center(50))
    print("=" * 50)
    for face in range(1, 7):
        c = counts[face]
        pct = (c / n) * 100
        bar = "█" * int(pct / 2)
        print(f"Face [{face}]: {c:>6} ({pct:>5.1f}%) | {bar}")
    print("=" * 50)

def main():
    print("=" * 50)
    print("🎲 DICE ROLLING SIMULATOR 🎲".center(50))
    print("=" * 50)

    while True:
        print("\nSelect Option:")
        print("1. Interactive Dice Roller (with ASCII Dice)")
        print("2. Large Scale Statistical Simulator")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()
        if choice == "1":
            interactive_roll()
        elif choice == "2":
            run_simulation()
        elif choice == "3":
            print("\nThanks for rolling! See you! 👋\n")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
