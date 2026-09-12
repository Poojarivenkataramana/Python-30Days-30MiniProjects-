# ----------------------------------------------------
# Day 23: Flashcard Study Quizzer
# Concepts: JSON File I/O, Lists of Dictionaries, Interactive Prompting, Active Recall
# ----------------------------------------------------

import json
import os
import random

DATA_FILE = "flashcards.json"

DEFAULT_DECKS = {
    "Python Basics": [
        {"q": "What data structure uses key-value pairs?", "a": "Dictionary (dict)"},
        {"q": "How do you create an anonymous one-line function?", "a": "Using the 'lambda' keyword"},
        {"q": "What method removes and returns the last item of a list?", "a": "list.pop()"},
        {"q": "What is the output of bool([])?", "a": "False (Empty collections are falsy)"},
        {"q": "Which operator performs integer floor division?", "a": "// (double slash)"}
    ],
    "World Capitals": [
        {"q": "What is the capital of Japan?", "a": "Tokyo"},
        {"q": "What is the capital of France?", "a": "Paris"},
        {"q": "What is the capital of Australia?", "a": "Canberra"},
        {"q": "What is the capital of Canada?", "a": "Ottawa"}
    ]
}

def load_decks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return DEFAULT_DECKS
    else:
        save_decks(DEFAULT_DECKS)
        return DEFAULT_DECKS

def save_decks(decks):
    with open(DATA_FILE, "w") as f:
        json.dump(decks, f, indent=4)

def study_deck(decks):
    print("\nAvailable Decks:")
    deck_names = list(decks.keys())
    for i, name in enumerate(deck_names, 1):
        print(f"{i}. {name} ({len(decks[name])} cards)")

    try:
        choice = int(input("\nSelect deck to study (number): "))
        if not (1 <= choice <= len(deck_names)):
            print("❌ Invalid deck number.")
            return
        selected_deck = deck_names[choice - 1]
    except ValueError:
        print("❌ Invalid input.")
        return

    cards = decks[selected_deck][:]
    random.shuffle(cards)

    correct_count = 0
    total = len(cards)

    print("\n" + "=" * 50)
    print(f"📖 STUDYING: {selected_deck.upper()} 📖".center(50))
    print("=" * 50)

    for i, card in enumerate(cards, 1):
        print(f"\n[Card {i}/{total}]")
        print(f"❓ QUESTION: {card['q']}")
        input("👉 Press [Enter] to reveal the answer...")
        print(f"💡 ANSWER  : {card['a']}")

        eval_input = input("Did you know this? (y/n): ").strip().lower()
        if eval_input in ("y", "yes"):
            correct_count += 1
            print("✅ Great job!")
        else:
            print("📝 Keep practicing this card.")
        print("-" * 50)

    pct = (correct_count / total) * 100 if total > 0 else 0
    print("\n" + "=" * 50)
    print("📊 SESSION SUMMARY 📊".center(50))
    print("=" * 50)
    print(f"Total Cards Reviewed : {total}")
    print(f"Correctly Recalled   : {correct_count}")
    print(f"Retention Score      : {pct:.1f}%")
    print("=" * 50)

def add_new_card(decks):
    print("\nAvailable Decks:")
    deck_names = list(decks.keys())
    for i, name in enumerate(deck_names, 1):
        print(f"{i}. {name}")
    print(f"{len(deck_names) + 1}. Create a NEW Deck")

    try:
        choice = int(input("\nSelect deck (number): "))
        if choice == len(deck_names) + 1:
            new_deck_name = input("Enter new deck name: ").strip()
            if not new_deck_name:
                return
            decks[new_deck_name] = []
            selected_deck = new_deck_name
        elif 1 <= choice <= len(deck_names):
            selected_deck = deck_names[choice - 1]
        else:
            print("❌ Invalid choice.")
            return
    except ValueError:
        return

    q = input("\nEnter Question/Prompt: ").strip()
    a = input("Enter Answer/Explanation: ").strip()

    if q and a:
        decks[selected_deck].append({"q": q, "a": a})
        save_decks(decks)
        print(f"✅ Added card to '{selected_deck}'!")

def main():
    decks = load_decks()

    while True:
        print("\n" + "=" * 40)
        print("🗂️ FLASHCARD STUDY QUIZZER 🗂️".center(40))
        print("=" * 40)
        print("1. Study a Deck")
        print("2. Add Card / Create Deck")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()
        if choice == "1":
            study_deck(decks)
        elif choice == "2":
            add_new_card(decks)
        elif choice == "3":
            print("\nHappy studying! Goodbye! 🎓\n")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
