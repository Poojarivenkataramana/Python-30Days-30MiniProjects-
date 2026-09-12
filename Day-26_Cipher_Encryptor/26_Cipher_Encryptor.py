# ----------------------------------------------------
# Day 26: Classical Cipher Encryption & Decryption
# Concepts: ASCII Character Codes (ord / chr), Modular Arithmetic, Cryptography
# ----------------------------------------------------

def caesar_encrypt(text, shift):
    result = []
    shift = shift % 26
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + shift) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_brute_force(text):
    print("\n" + "-" * 50)
    print("🔓 CAESAR CIPHER BRUTE-FORCE (ALL 25 SHIFTS) 🔓")
    print("-" * 50)
    for s in range(1, 26):
        decrypted = caesar_decrypt(text, s)
        print(f"Shift {s:>2}: {decrypted}")
    print("-" * 50)

def vigenere_encrypt(text, key):
    result = []
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 97
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 97
            if char.isupper():
                result.append(chr((ord(char) - 65 - shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - shift) % 26 + 97))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def main():
    print("=" * 50)
    print("🔐 CIPHER ENCRYPTION & DECRYPTION TOOL 🔐".center(50))
    print("=" * 50)

    while True:
        print("\nChoose Cipher Tool:")
        print("1. Caesar Cipher (Encrypt)")
        print("2. Caesar Cipher (Decrypt)")
        print("3. Caesar Cipher (Brute-Force All Shifts)")
        print("4. Vigenère Cipher (Encrypt)")
        print("5. Vigenère Cipher (Decrypt)")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice in ("1", "2"):
            msg = input("\nEnter text: ")
            try:
                shift = int(input("Enter integer shift key (e.g. 3): "))
            except ValueError:
                print("❌ Invalid shift integer.")
                continue

            if choice == "1":
                out = caesar_encrypt(msg, shift)
                print(f"\n🔒 Encrypted Text: {out}")
            else:
                out = caesar_decrypt(msg, shift)
                print(f"\n🔓 Decrypted Text: {out}")

        elif choice == "3":
            msg = input("\nEnter encrypted ciphertext to crack: ")
            caesar_brute_force(msg)

        elif choice == "4":
            msg = input("\nEnter plaintext: ")
            key = input("Enter alphabetical keyword: ").strip()
            if not key.isalpha():
                print("❌ Key must contain only letters.")
                continue
            out = vigenere_encrypt(msg, key)
            print(f"\n🔒 Encrypted Text: {out}")

        elif choice == "5":
            msg = input("\nEnter ciphertext: ")
            key = input("Enter alphabetical keyword: ").strip()
            if not key.isalpha():
                print("❌ Key must contain only letters.")
                continue
            out = vigenere_decrypt(msg, key)
            print(f"\n🔓 Decrypted Text: {out}")

        elif choice == "6":
            print("\nStay secure! Goodbye! 🛡️\n")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
