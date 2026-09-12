# ----------------------------------------------------
# Day 05: Rock, Paper, Scissors Game
# Concepts: Random module (random.choice), Dictionaries, Loops, Score Tracking
# ----------------------------------------------------

import random

# ASCII Art for choices
ICONS = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

CHOICES = ["rock", "paper", "scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play():
    print("=" * 50)
    print("✊ ✋ ✌️  ROCK - PAPER - SCISSORS  ✊ ✋ ✌️".center(50))
    print("=" * 50)

    user_score = 0
    computer_score = 0
    ties = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        print("Choose: [R]ock, [P]aper, [S]cissors or [Q]uit")
        user_input = input("Your Choice: ").strip().lower()

        if user_input in ("q", "quit", "exit"):
            break

        mapping = {"r": "rock", "p": "paper", "s": "scissors"}
        user_choice = mapping.get(user_input, user_input)

        if user_choice not in CHOICES:
            print("❌ Invalid choice! Please enter Rock, Paper, Scissors, or R, P, S.")
            continue

        computer_choice = random.choice(CHOICES)

        print("\nYour Move:")
        print(ICONS[user_choice])
        print("Computer's Move:")
        print(ICONS[computer_choice])

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            ties += 1
            print("🤝 It's a Tie!")
        elif result == "user":
            user_score += 1
            print("🎉 You Win this round!")
        else:
            computer_score += 1
            print("🤖 Computer Wins this round!")

        round_num += 1
        print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score} | Ties: {ties}")

    print("\n" + "=" * 50)
    print("FINAL SCORECARD".center(50))
    print("=" * 50)
    print(f"Total Rounds Played : {round_num - 1}")
    print(f"Your Score          : {user_score}")
    print(f"Computer Score      : {computer_score}")
    print(f"Ties                : {ties}")

    if user_score > computer_score:
        print("\n🏆 CONGRATULATIONS! You are the overall Champion! 🏆")
    elif user_score < computer_score:
        print("\n💻 Better luck next time! Computer won the match.")
    else:
        print("\n🤝 The match ended in an overall Draw!")
    print("=" * 50)

if __name__ == "__main__":
    play()
