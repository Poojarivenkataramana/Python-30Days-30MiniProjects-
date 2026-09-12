# ----------------------------------------------------
# Day 14: Palindrome & Anagram Checker
# Concepts: String Slicing [::-1], Character Sorting, Regular Expressions, Sanitization
# ----------------------------------------------------

import re

def clean_string(s):
    # Keep only alphanumeric characters and convert to lower case
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def check_palindrome(text):
    cleaned = clean_string(text)
    if not cleaned:
        return False, "", ""
    reversed_str = cleaned[::-1]
    is_pal = (cleaned == reversed_str)
    return is_pal, cleaned, reversed_str

def check_anagram(str1, str2):
    cleaned1 = clean_string(str1)
    cleaned2 = clean_string(str2)
    if not cleaned1 or not cleaned2:
        return False
    return sorted(cleaned1) == sorted(cleaned2)

def main():
    print("=" * 50)
    print("🔤 PALINDROME & ANAGRAM CHECKER 🔤".center(50))
    print("=" * 50)

    while True:
        print("\nSelect Option:")
        print("1. Check Palindrome (Word or Phrase)")
        print("2. Check Anagram (Compare Two Strings)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            text = input("\nEnter word or sentence: ").strip()
            is_pal, cleaned, rev = check_palindrome(text)
            print("\n" + "-" * 45)
            print(f"Original Text   : \"{text}\"")
            print(f"Sanitized Text  : \"{cleaned}\"")
            print(f"Reversed Text   : \"{rev}\"")
            if is_pal:
                print("🎉 Result: It IS a Palindrome! ✅")
            else:
                print("❌ Result: NOT a Palindrome.")
            print("-" * 45)

        elif choice == "2":
            s1 = input("\nEnter First Word/Phrase : ").strip()
            s2 = input("Enter Second Word/Phrase: ").strip()
            is_ana = check_anagram(s1, s2)
            print("\n" + "-" * 45)
            print(f"String 1: \"{s1}\"")
            print(f"String 2: \"{s2}\"")
            if is_ana:
                print("🎉 Result: They ARE Anagrams of each other! ✅")
            else:
                print("❌ Result: NOT Anagrams.")
            print("-" * 45)

        elif choice == "3":
            print("\nThanks for using String Checker! Goodbye! 👋\n")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
