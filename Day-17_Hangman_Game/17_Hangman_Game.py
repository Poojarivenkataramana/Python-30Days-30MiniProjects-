# ----------------------------------------------------
# Day 17: Hangman Word Guessing Game
# Concepts: Strings, Sets, ASCII Art, Game Loop State Machine
# ----------------------------------------------------

import random

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

WORD_CATEGORIES = {
    "Programming": ["PYTHON", "JAVASCRIPT", "DEVELOPER", "VARIABLE", "FUNCTION", "DATABASE", "ALGORITHM"],
    "Animals": ["ELEPHANT", "KANGAROO", "DOLPHIN", "CHEETAH", "PENGUIN", "GIRAFFE", "OCTOPUS"],
    "Countries": ["CANADA", "BRAZIL", "GERMANY", "JAPAN", "AUSTRALIA", "INDIA", "SINGAPORE"]
}

def play_hangman():
    print("=" * 50)
    print("🪢 HANGMAN WORD GAME 🪢".center(50))
    print("=" * 50)

    category = random.choice(list(WORD_CATEGORIES.keys()))
    secret_word = random.choice(WORD_CATEGORIES[category])
    
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print(f"\n💡 Category Hint: {category}")
    print(f"The word has {len(secret_word)} letters.\n")

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])

        # Display word progress
        display_word = [ch if ch in guessed_letters else "_" for ch in secret_word]
        print(f"Word: {' '.join(display_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Lives: {max_wrong - wrong_guesses}")

        # Check win condition
        if "_" not in display_word:
            print("\n" + "*" * 50)
            print(f"🎉 CONGRATULATIONS! You guessed the word: {secret_word} 🎉".center(50))
            print("*" * 50)
            return

        guess = input("\nGuess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Oops! '{guess}' is NOT in the word.")

    # If loop finishes with max wrong guesses
    print(HANGMAN_PICS[max_wrong])
    print("-" * 50)
    print(f"💀 GAME OVER! You ran out of lives.")
    print(f"The secret word was: {secret_word}")
    print("-" * 50)

def main():
    while True:
        play_hangman()
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            print("\nThanks for playing Hangman! Goodbye! 👋\n")
            break

if __name__ == "__main__":
    main()
