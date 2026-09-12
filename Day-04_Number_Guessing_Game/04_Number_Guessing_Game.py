# ----------------------------------------------------
# Day 04: Number Guessing Game
# Concepts: Random module, While loops, Conditionals, User Input, Attempt tracking
# ----------------------------------------------------

import random

def play_game():
    print("=" * 45)
    print("🎯 NUMBER GUESSING GAME 🎯".center(45))
    print("=" * 45)
    print("I have chosen a secret number between 1 and 100.")
    print("Can you guess it within the allowed attempts?\n")

    # Select difficulty level
    print("Select Difficulty Level:")
    print("1. Easy   (10 Attempts)")
    print("2. Medium (7 Attempts)")
    print("3. Hard   (5 Attempts)")

    attempts_allowed = 7
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice == "1":
            attempts_allowed = 10
            break
        elif choice == "2":
            attempts_allowed = 7
            break
        elif choice == "3":
            attempts_allowed = 5
            break
        else:
            print("❌ Invalid selection! Please enter 1, 2, or 3.")

    secret_number = random.randint(1, 100)
    attempts_used = 0
    won = False

    print(f"\nGame Started! You have {attempts_allowed} attempts. Good luck! 🚀")
    print("-" * 45)

    while attempts_used < attempts_allowed:
        remaining = attempts_allowed - attempts_used
        user_input = input(f"\n[Attempt {attempts_used + 1}/{attempts_allowed}] Enter your guess (1-100): ").strip()

        # Input validation
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter an integer between 1 and 100.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("❌ Out of range! Guess must be between 1 and 100.")
            continue

        attempts_used += 1

        if guess == secret_number:
            won = True
            print("\n" + "*" * 45)
            print(f"🎉 BINGO! You guessed the number {secret_number} correctly in {attempts_used} attempts! 🎉".center(45))
            print("*" * 45)
            break
        elif guess < secret_number:
            diff = secret_number - guess
            hint = "(🔥 Very Close!)" if diff <= 5 else ""
            print(f"📉 Too LOW! {hint}")
        else:
            diff = guess - secret_number
            hint = "(🔥 Very Close!)" if diff <= 5 else ""
            print(f"📈 Too HIGH! {hint}")

    if not won:
        print("\n" + "-" * 45)
        print(f"😢 Game Over! You've used all {attempts_allowed} attempts.")
        print(f"The secret number was: {secret_number}")
        print("-" * 45)

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nThanks for playing! See you next time! 👋\n")
            break

if __name__ == "__main__":
    main()
