# ----------------------------------------------------
# Day 30: Secure Personal Diary & Journal
# Concepts: hashlib (SHA-256 Authentication), JSON Storage, Datetime, Search Filters
# ----------------------------------------------------

import hashlib
import json
import os
from datetime import datetime

DIARY_FILE = "diary.json"

def hash_password(pwd):
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()

def load_diary():
    if os.path.exists(DIARY_FILE):
        try:
            with open(DIARY_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"password_hash": None, "entries": []}
    return {"password_hash": None, "entries": []}

def save_diary(data):
    with open(DIARY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def authenticate(data):
    if not data.get("password_hash"):
        print("\n🔒 Setup Master Password for your Diary:")
        pwd1 = input("Create Password: ").strip()
        pwd2 = input("Confirm Password: ").strip()
        if pwd1 != pwd2 or not pwd1:
            print("❌ Passwords do not match or empty! Try again.")
            return False
        data["password_hash"] = hash_password(pwd1)
        save_diary(data)
        print("✅ Master Password configured successfully!")
        return True

    print("\n🔒 Diary is Locked.")
    for attempt in range(3):
        pwd = input("Enter Master Password: ").strip()
        if hash_password(pwd) == data["password_hash"]:
            print("🔓 Access Granted!")
            return True
        else:
            print(f"❌ Incorrect password! ({2 - attempt} attempts remaining)")
    return False

def add_entry(data):
    print("\n--- ✍️ New Journal Entry ---")
    title = input("Entry Title: ").strip()
    if not title:
        title = "Untitled Entry"

    print("Choose Mood: 1. 😊 Happy  2. 💡 Inspired  3. 🧘 Calm  4. 😴 Tired  5. 😔 Sad")
    mood_map = {"1": "😊 Happy", "2": "💡 Inspired", "3": "🧘 Calm", "4": "😴 Tired", "5": "😔 Sad"}
    mood_choice = input("Mood [1-5]: ").strip()
    mood = mood_map.get(mood_choice, "📝 Neutral")

    print("\nWrite your entry below (Press Enter on an empty line to finish):")
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    content = "\n".join(lines)
    if not content.strip():
        print("❌ Entry content cannot be empty.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "id": len(data["entries"]) + 1,
        "timestamp": timestamp,
        "title": title,
        "mood": mood,
        "content": content
    }

    data["entries"].append(entry)
    save_diary(data)
    print("✅ Entry securely saved to your diary!")

def view_entries(data):
    entries = data.get("entries", [])
    print("\n" + "=" * 60)
    print("📖 PERSONAL DIARY ENTRIES 📖".center(60))
    print("=" * 60)
    if not entries:
        print("No diary entries found yet.")
        print("=" * 60)
        return

    for e in reversed(entries):
        print(f"\n🗓️  Date : {e['timestamp']}  |  Mood: {e.get('mood', 'Neutral')}")
        print(f"📌 Title: {e['title']}")
        print("-" * 60)
        print(e["content"])
        print("=" * 60)

def search_entries(data):
    keyword = input("\nEnter search keyword: ").strip().lower()
    if not keyword:
        return

    matches = [e for e in data.get("entries", []) if keyword in e["title"].lower() or keyword in e["content"].lower()]
    print("\n" + "-" * 50)
    print(f"🔍 Search Results for '{keyword}': ({len(matches)} found)")
    print("-" * 50)
    for e in matches:
        print(f"[{e['timestamp']}] {e['title']} - {e['content'][:60]}...")
    print("-" * 50)

def main():
    print("=" * 50)
    print("📖 SECURE PERSONAL DIARY & JOURNAL 📖".center(50))
    print("=" * 50)

    data = load_diary()

    if not authenticate(data):
        print("\n❌ Authentication failed. Exiting.")
        return

    while True:
        print("\n" + "=" * 40)
        print("📔 DIARY DASHBOARD 📔".center(40))
        print("=" * 40)
        print("1. Write New Entry")
        print("2. Read All Entries")
        print("3. Search Entries by Keyword")
        print("4. Lock & Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            search_entries(data)
        elif choice == "4":
            print("\n🔒 Diary safely locked. Have a wonderful day! 👋\n")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
