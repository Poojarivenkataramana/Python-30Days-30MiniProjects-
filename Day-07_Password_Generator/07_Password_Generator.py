# ----------------------------------------------------
# Day 07: Secure Password Generator & Strength Checker
# Concepts: string module, random / secrets module, List Comprehensions, Logic
# ----------------------------------------------------

import random
import string

def check_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if len(pwd) >= 12: score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1

    if score <= 2:
        return "Weak ⚠️"
    elif score <= 4:
        return "Moderate 🟡"
    elif score <= 5:
        return "Strong 🟢"
    else:
        return "Very Strong / Ironclad 🛡️"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    chars = ""
    guaranteed = []

    if use_upper:
        chars += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        chars += string.ascii_lowercase
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        chars += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        chars += string.punctuation
        guaranteed.append(random.choice(string.punctuation))

    if not chars:
        return None

    # Fill the remaining length
    remaining_length = length - len(guaranteed)
    random_chars = [random.choice(chars) for _ in range(remaining_length)]
    
    password_list = guaranteed + random_chars
    random.shuffle(password_list)
    return "".join(password_list)

def main():
    print("=" * 50)
    print("🔐 SECURE PASSWORD GENERATOR 🔐".center(50))
    print("=" * 50)

    try:
        length_input = input("Enter password length (minimum 6, default 12): ").strip()
        length = int(length_input) if length_input else 12
        if length < 6:
            print("❌ Length must be at least 6 characters.")
            return
        if length > 128:
            print("❌ Length cannot exceed 128 characters.")
            return
    except ValueError:
        print("❌ Invalid integer value for length.")
        return

    print("\nInclude character sets (y/n)?")
    inc_upper = input("Include Uppercase letters (A-Z)? [y/n, default y]: ").strip().lower() != "n"
    inc_lower = input("Include Lowercase letters (a-z)? [y/n, default y]: ").strip().lower() != "n"
    inc_digits = input("Include Numbers (0-9)? [y/n, default y]: ").strip().lower() != "n"
    inc_symbols = input("Include Symbols (@#$%...)? [y/n, default y]: ").strip().lower() != "n"

    if not (inc_upper or inc_lower or inc_digits or inc_symbols):
        print("❌ Error: You must select at least one character type!")
        return

    try:
        count_input = input("\nHow many passwords to generate? (default 1): ").strip()
        count = int(count_input) if count_input else 1
    except ValueError:
        count = 1

    print("\n" + "-" * 50)
    print("GENERATED PASSWORDS".center(50))
    print("-" * 50)

    for i in range(count):
        pwd = generate_password(length, inc_upper, inc_lower, inc_digits, inc_symbols)
        strength = check_strength(pwd)
        print(f"[{i+1}] {pwd}")
        print(f"    Strength: {strength}\n")
    print("-" * 50)

if __name__ == "__main__":
    main()
