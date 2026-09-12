# ----------------------------------------------------
# Day 08: Word & Character Text Analyzer
# Concepts: String Manipulation, Lists, Dictionaries, Collections, Text Processing
# ----------------------------------------------------

from collections import Counter
import re

def analyze_text(text):
    if not text.strip():
        print("❌ The provided text is empty!")
        return

    # Basic Metrics
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    
    # Words
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    
    # Sentences and Lines
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)
    lines = text.splitlines()
    line_count = len(lines)

    # Average word length
    avg_word_len = round(sum(len(w) for w in words) / word_count, 2) if word_count > 0 else 0
    
    # Word frequencies
    word_freq = Counter(words).most_common(5)

    # Vowels vs Consonants
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    digits = sum(1 for c in text if c.isdigit())

    print("\n" + "=" * 45)
    print("📊 TEXT ANALYSIS REPORT 📊".center(45))
    print("=" * 45)
    print(f"{'Total Characters (all)':<25}: {char_count_with_spaces}")
    print(f"{'Characters (no spaces)':<25}: {char_count_no_spaces}")
    print(f"{'Total Words':<25}: {word_count}")
    print(f"{'Total Sentences':<25}: {sentence_count}")
    print(f"{'Total Lines':<25}: {line_count}")
    print(f"{'Average Word Length':<25}: {avg_word_len} chars")
    print(f"{'Vowels / Consonants':<25}: {vowels} / {consonants}")
    print(f"{'Digits Count':<25}: {digits}")
    
    print("\n--- 🔝 Top 5 Most Frequent Words ---")
    if word_freq:
        for idx, (word, freq) in enumerate(word_freq, 1):
            print(f"  {idx}. '{word}': {freq} time(s)")
    else:
        print("  No words found.")
    print("=" * 45)

def main():
    print("=" * 45)
    print("📝 WORD & CHARACTER COUNTER 📝".center(45))
    print("=" * 45)
    print("1. Enter text interactively")
    print("2. Analyze a sample paragraph")

    choice = input("\nEnter choice (1/2): ").strip()

    if choice == "1":
        print("\nEnter/Paste your text below (Press Enter on empty line to finish):")
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        sample = "\n".join(lines)
    else:
        sample = (
            "Python is an easy to learn, powerful programming language. "
            "It has efficient high-level data structures and a simple but effective approach to object-oriented programming. "
            "Python's elegant syntax and dynamic typing make it an ideal language for scripting and rapid application development."
        )
        print(f"\nAnalyzing default sample text:\n\"{sample}\"")

    analyze_text(sample)

if __name__ == "__main__":
    main()
