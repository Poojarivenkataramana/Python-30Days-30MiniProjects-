# ----------------------------------------------------
# Day 13: Morse Code Translator (Bidirectional)
# Concepts: Dictionaries (Key-Value Inversion), String Parsing, Encoding/Decoding
# ----------------------------------------------------

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', 
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {val: key for key, val in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')
    return ' '.join(morse)

def morse_to_text(morse_code):
    words = morse_code.strip().split(' / ')
    decoded_message = []
    
    for word in words:
        letters = word.split(' ')
        decoded_word = ""
        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                decoded_word += REVERSE_MORSE_DICT[letter]
            elif letter == '':
                continue
            else:
                decoded_word += '?'
        decoded_message.append(decoded_word)
        
    return ' '.join(decoded_message)

def main():
    print("=" * 50)
    print("📡 MORSE CODE TRANSLATOR 📡".center(50))
    print("=" * 50)

    while True:
        print("\nChoose Translation Mode:")
        print("1. Text to Morse Code (English -> Morse)")
        print("2. Morse Code to Text (Morse -> English)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            text = input("\nEnter English text: ").strip()
            if not text:
                print("❌ Input cannot be empty.")
                continue
            encoded = text_to_morse(text)
            print("\n" + "-" * 50)
            print("🔊 Morse Code Output:")
            print(encoded)
            print("-" * 50)

        elif choice == "2":
            print("\nFormat Note: Use space between letters and ' / ' between words (e.g. '... --- ... / .--. -.-- - .... --- -.')")
            morse = input("Enter Morse code: ").strip()
            if not morse:
                print("❌ Input cannot be empty.")
                continue
            decoded = morse_to_text(morse)
            print("\n" + "-" * 50)
            print("📄 Decoded English Text:")
            print(decoded)
            print("-" * 50)

        elif choice == "3":
            print("\nGoodbye! Over and Out! 📻\n")
            break
        else:
            print("❌ Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
