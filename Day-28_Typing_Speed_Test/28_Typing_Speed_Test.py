# ----------------------------------------------------
# Day 28: Typing Speed & Accuracy Tester
# Concepts: time module, String Metrics, WPM formula, Accuracy comparison
# ----------------------------------------------------

import time
import random

PROMPTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a clear and powerful object oriented programming language.",
    "Consistency is the key to mastering any programming skill.",
    "Beautiful is better than ugly, explicit is better than implicit.",
    "Simple is better than complex, complex is better than complicated."
]

def calculate_accuracy(original, typed):
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    total_chars = max(len(original), len(typed))
    if total_chars == 0:
        return 0.0
    return (correct_chars / total_chars) * 100

def run_test():
    prompt = random.choice(PROMPTS)
    
    print("=" * 60)
    print("⌨️  TYPING SPEED & ACCURACY TEST  ⌨️".center(60))
    print("=" * 60)
    print("Type the following sentence exactly as shown and press Enter:")
    print("-" * 60)
    print(f"👉 \"{prompt}\"")
    print("-" * 60)

    input("\nPress [ENTER] when you are ready to start...")
    print("\n🟢 START TYPING NOW!\n")

    start_time = time.time()
    user_input = input(">> ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60

    word_count = len(user_input.split())
    wpm = (word_count / minutes) if minutes > 0 else 0
    accuracy = calculate_accuracy(prompt, user_input)

    print("\n" + "=" * 60)
    print("📊 YOUR TYPING SCORECARD 📊".center(60))
    print("=" * 60)
    print(f"{'Time Elapsed':<25}: {elapsed_time:.2f} seconds")
    print(f"{'Words Typed':<25}: {word_count} words")
    print(f"{'Gross Speed (WPM)':<25}: {wpm:.1f} WPM")
    print(f"{'Accuracy Score':<25}: {accuracy:.1f}%")
    print("-" * 60)

    if accuracy >= 95 and wpm >= 50:
        print("🌟 Rank: Master Typist! Incredible speed and accuracy! 🚀")
    elif accuracy >= 85 and wpm >= 35:
        print("👏 Rank: Intermediate Typist! Solid typing performance! 👍")
    else:
        print("📚 Rank: Apprentice! Practice makes perfect! 💪")
    print("=" * 60)

def main():
    while True:
        run_test()
        replay = input("\nWould you like to try another test? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nThanks for testing your speed! Keep practicing! 👋\n")
            break

if __name__ == "__main__":
    main()
