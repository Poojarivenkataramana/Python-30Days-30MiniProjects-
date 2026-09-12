# ----------------------------------------------------
# Day 19: Text-Based RPG Adventure Game
# Concepts: State Management, Decision Trees, Inventory Systems, Function Modularity
# ----------------------------------------------------

import time
import random

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def start_game():
    player = {
        "name": "",
        "hp": 100,
        "inventory": ["Torch"],
        "has_treasure": False
    }

    print("=" * 55)
    print("🗡️  THE MYSTERIOUS DUNGEON OF ELDORIA  🗡️".center(55))
    print("=" * 55)

    name = input("Enter your Hero's Name: ").strip()
    player["name"] = name if name else "Adventurer"

    slow_print(f"\nWelcome, {player['name']}! You stand before the ancient stone entrance of Eldoria.")
    slow_print("Legends speak of a hidden Golden Relic buried deep within...")

    entrance_choice(player)

def entrance_choice(player):
    print("\n" + "-" * 50)
    print("You see two passages ahead:")
    print("1. Take the Left stone archway (Damp and echoing)")
    print("2. Take the Right narrow corridor (Faintly glowing with moss)")
    print("3. Check your inventory")

    while True:
        choice = input("\nWhat will you do? (1/2/3): ").strip()
        if choice == "1":
            left_chamber(player)
            break
        elif choice == "2":
            right_corridor(player)
            break
        elif choice == "3":
            print(f"🎒 Inventory: {', '.join(player['inventory'])} | HP: {player['hp']}/100")
        else:
            print("❌ Invalid action. Choose 1, 2, or 3.")

def left_chamber(player):
    slow_print("\nYou enter a massive, damp cavern. Water drips from stalactites.")
    slow_print("A wild Goblin jumps out from behind a rock with a rusted dagger! 👺")

    print("\n1. Fight the Goblin with your bare hands")
    print("2. Use your Torch to scare him off")
    print("3. Run back to the entrance")

    choice = input("\nChoose your move (1/2/3): ").strip()

    if choice == "1":
        damage = random.randint(25, 45)
        player["hp"] -= damage
        slow_print(f"\nYou wrestled the Goblin and won, but took {damage} damage! (Current HP: {player['hp']})")
        if player["hp"] <= 0:
            game_over(player, "You collapsed from your wounds.")
            return
        slow_print("The Goblin dropped an Ancient Silver Key! 🗝️")
        player["inventory"].append("Silver Key")
        treasure_room(player)

    elif choice == "2":
        if "Torch" in player["inventory"]:
            slow_print("\nYou wave the blazing Torch! The goblin shatters in fear and flees!")
            slow_print("You find an Ancient Silver Key on the ground! 🗝️")
            player["inventory"].append("Silver Key")
            treasure_room(player)
        else:
            slow_print("You don't have a torch!")
            left_chamber(player)
    else:
        slow_print("\nYou safely retreat back.")
        entrance_choice(player)

def right_corridor(player):
    slow_print("\nThe luminous moss lights up the corridor gently.")
    slow_print("You stumble upon an alchemist's shrine with a glowing Red Potion 🧪.")

    print("\n1. Drink the potion immediately")
    print("2. Put the potion in your inventory")
    print("3. Ignore it and press forward")

    choice = input("\nChoose action (1/2/3): ").strip()

    if choice == "1":
        player["hp"] = min(100, player["hp"] + 30)
        slow_print(f"✨ A warm vitality rushes through you! Your HP is restored to {player['hp']}.")
    elif choice == "2":
        player["inventory"].append("Healing Potion")
        slow_print("🧪 Healing Potion added to your backpack.")

    slow_print("You continue walking and find a locked ornate vault door...")
    treasure_room(player)

def treasure_room(player):
    print("\n" + "=" * 50)
    slow_print("🏛️ You stand before the Ancient Golden Vault 🏛️")
    print("=" * 50)

    if "Silver Key" in player["inventory"]:
        slow_print("You insert the Silver Key into the vault lock... *CLICK!*")
        slow_print("The heavy stone doors slide open to reveal the legendary Golden Relic! 👑✨")
        victory(player)
    else:
        slow_print("The door is locked with an ancient keyhole.")
        print("\n1. Try to bash the door open")
        print("2. Search other paths for the key")

        choice = input("\nChoose (1/2): ").strip()
        if choice == "1":
            damage = 40
            player["hp"] -= damage
            slow_print(f"You charge the solid stone door! You bruised your shoulder for {damage} HP (HP: {player['hp']}).")
            if player["hp"] <= 0:
                game_over(player, "You exhausted your last strength trying to force the unbreakable door.")
            else:
                entrance_choice(player)
        else:
            entrance_choice(player)

def victory(player):
    print("\n" + "*" * 55)
    print("🏆 VICTORY! YOU HAVE CONQUERED THE DUNGEON! 🏆".center(55))
    print("*" * 55)
    print(f"Hero Name       : {player['name']}")
    print(f"Remaining HP    : {player['hp']}/100")
    print(f"Inventory Items : {', '.join(player['inventory'])}")
    print("\nYou return to the village as a celebrated legend! 🎉\n")

def game_over(player, reason):
    print("\n" + "=" * 50)
    print("💀 GAME OVER 💀".center(50))
    print("=" * 50)
    print(f"Reason: {reason}")
    print(f"{player['name']}'s journey ended here.\n")

def main():
    while True:
        start_game()
        replay = input("Play another adventure? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nFarewell, brave adventurer! 🛡️\n")
            break

if __name__ == "__main__":
    main()
