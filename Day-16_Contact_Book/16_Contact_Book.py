# ----------------------------------------------------
# Day 16: Contact Book Management System
# Concepts: OOP / Classes, Dictionaries, Searching/Filtering, JSON Storage
# ----------------------------------------------------

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    print("\n--- 👤 Add New Contact ---")
    name = input("Enter Full Name: ").strip()
    if not name:
        print("❌ Contact name is required.")
        return

    # Check if contact already exists
    for c in contacts:
        if c["name"].lower() == name.lower():
            print("⚠️ A contact with this name already exists!")
            return

    phone = input("Enter Phone Number: ").strip()
    if not phone.replace("+", "").replace("-", "").replace(" ", "").isdigit():
        print("❌ Invalid phone number format.")
        return

    email = input("Enter Email Address: ").strip()
    address = input("Enter City/Address: ").strip()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "N/A",
        "address": address if address else "N/A"
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✅ Contact '{name}' saved successfully!")

def view_all_contacts(contacts):
    print("\n" + "=" * 65)
    print("📖 ALL CONTACTS 📖".center(65))
    print("=" * 65)
    if not contacts:
        print("No contacts in your address book yet.")
        print("=" * 65)
        return

    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())
    print(f"{'#':<4} {'Name':<20} {'Phone':<16} {'Email'}")
    print("-" * 65)
    for i, c in enumerate(sorted_contacts, 1):
        print(f"{i:<4} {c['name']:<20} {c['phone']:<16} {c['email']}")
    print("=" * 65)

def search_contact(contacts):
    query = input("\nEnter search query (Name or Phone): ").strip().lower()
    if not query:
        return

    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]

    print("\n" + "-" * 50)
    print(f"🔍 Search Results for '{query}': ({len(results)} found)")
    print("-" * 50)
    if not results:
        print("No matching contacts found.")
    else:
        for c in results:
            print(f"👤 Name    : {c['name']}")
            print(f"📞 Phone   : {c['phone']}")
            print(f"📧 Email   : {c['email']}")
            print(f"🏠 Address : {c['address']}")
            print("-" * 30)

def delete_contact(contacts):
    name = input("\nEnter exact name of contact to delete: ").strip().lower()
    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            removed = contacts.pop(i)
            save_contacts(contacts)
            print(f"🗑️ Contact '{removed['name']}' deleted.")
            return
    print("❌ Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n" + "=" * 40)
        print("📒 CONTACT BOOK MANAGER 📒".center(40))
        print("=" * 40)
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nSelect option (1-5): ").strip()

        if choice == "1":
            view_all_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nGoodbye! Stay connected! 📱\n")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
