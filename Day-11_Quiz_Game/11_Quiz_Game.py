# ----------------------------------------------------
# Day 11: Interactive Quiz Master
# Concepts: Dictionaries, Lists of Objects, Loops, Score Keeping, Input Validation
# ----------------------------------------------------

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B",
        "explanation": "'def' is the reserved keyword used to define functions in Python."
    },
    {
        "question": "What data type is the result of 3 / 2 in Python 3?",
        "options": ["A) int", "B) float", "C) double", "D) decimal"],
        "answer": "B",
        "explanation": "Standard division '/' in Python 3 always returns a float (1.5)."
    },
    {
        "question": "Which collection data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C",
        "explanation": "Tuples cannot be modified after creation, making them immutable."
    },
    {
        "question": "What does PEP 8 stand for in Python?",
        "options": ["A) Python Enterprise Protocol 8", "B) Python Enhancement Proposal 8", "C) Performance Enhancement Program 8", "D) Program Execution Protocol 8"],
        "answer": "B",
        "explanation": "PEP 8 is the official Style Guide for Python Code."
    },
    {
        "question": "Which method is used to add an item to the end of a list?",
        "options": ["A) push()", "B) insert()", "C) add()", "D) append()"],
        "answer": "D",
        "explanation": "'append()' inserts the specified element at the end of a list."
    }
]

def run_quiz():
    print("=" * 55)
    print("🧠 PYTHON INTERACTIVE QUIZ MASTER 🧠".center(55))
    print("=" * 55)
    print(f"Total Questions: {len(QUESTIONS)}")
    print("Answer each question by typing A, B, C, or D.\n")

    score = 0

    for i, q in enumerate(QUESTIONS, 1):
        print("-" * 55)
        print(f"Question {i}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")

        while True:
            ans = input("\nYour Answer (A/B/C/D): ").strip().upper()
            if ans in ("A", "B", "C", "D"):
                break
            print("❌ Invalid choice! Please enter A, B, C, or D.")

        if ans == q["answer"]:
            score += 1
            print("✅ Correct! 🎉")
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")
        print(f"💡 Info: {q['explanation']}\n")

    percentage = (score / len(QUESTIONS)) * 100

    print("=" * 55)
    print("🏆 FINAL QUIZ RESULTS 🏆".center(55))
    print("=" * 55)
    print(f"Questions Attempted : {len(QUESTIONS)}")
    print(f"Correct Answers     : {score}")
    print(f"Final Score         : {percentage:.1f}%")

    if percentage == 100:
        print("🌟 Outstanding! Perfect Score! 🌟")
    elif percentage >= 80:
        print("👏 Great Job! You have a solid grasp of Python.")
    elif percentage >= 60:
        print("👍 Good effort! Keep practicing to improve.")
    else:
        print("📚 Review the basics and try again! You can do it.")
    print("=" * 55)

if __name__ == "__main__":
    run_quiz()
