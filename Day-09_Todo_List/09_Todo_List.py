# ----------------------------------------------------
# Day 09: CLI To-Do List Application
# Concepts: List & Dictionary Manipulation, JSON File I/O, CRUD Operations
# ----------------------------------------------------

import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    print("\n" + "=" * 55)
    print("📋 CURRENT TO-DO LIST 📋".center(55))
    print("=" * 55)
    if not tasks:
        print("No tasks found! Your to-do list is clean. ✨")
    else:
        print(f"{'ID':<4} {'Status':<12} {'Priority':<10} {'Task Description'}")
        print("-" * 55)
        for i, t in enumerate(tasks, 1):
            status = "✅ Done" if t.get("done") else "⏳ Pending"
            priority = t.get("priority", "Medium")
            print(f"{i:<4} {status:<12} {priority:<10} {t.get('title')}")
    print("=" * 55)

def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if not title:
        print("❌ Task cannot be empty!")
        return

    print("Choose Priority: 1. Low  2. Medium  3. High (default: 2)")
    p_choice = input("Priority [1/2/3]: ").strip()
    priority_map = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priority_map.get(p_choice, "Medium")

    tasks.append({"title": title, "done": False, "priority": priority})
    save_tasks(tasks)
    print(f"✅ Task '{title}' added successfully!")

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print(f"🎉 Task '{tasks[idx]['title']}' marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: '{removed['title']}'")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 35)
        print("📝 TASK MANAGER MENU 📝".center(35))
        print("=" * 35)
        print("1. View Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Keep being productive! 🚀\n")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
