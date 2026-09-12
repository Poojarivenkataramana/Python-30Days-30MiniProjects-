# ----------------------------------------------------
# Day 12: Countdown Timer & Stopwatch
# Concepts: time module, formatted output (f-strings, \r carriage return), loop control
# ----------------------------------------------------

import time
import sys

def countdown_timer():
    print("\n--- ⏳ Countdown Timer ---")
    try:
        total_seconds = int(input("Enter countdown time in seconds (e.g. 10): "))
        if total_seconds <= 0:
            print("❌ Time must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid integer input.")
        return

    print("\nCountdown starting...")
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        timer_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time Left: {timer_str} ", end="", flush=True)
        time.sleep(1)
        total_seconds -= 1

    print("\r⏳ Time Left: 00:00:00 \n")
    print("🔔 Time's UP! 🔔\a")

def stopwatch():
    print("\n--- ⏱️ Stopwatch ---")
    input("Press ENTER to start the stopwatch...")
    start_time = time.time()
    lap_num = 1

    print("Stopwatch is running! (Press Ctrl+C to stop, or Enter for Lap)\n")
    try:
        while True:
            # Check elapsed
            input("Press [Enter] to record Lap (Ctrl+C to Stop): ")
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            millis = int((elapsed - int(elapsed)) * 100)
            print(f"🚩 Lap {lap_num}: {mins:02d}:{secs:02d}.{millis:02d}")
            lap_num += 1
    except KeyboardInterrupt:
        total = time.time() - start_time
        mins, secs = divmod(int(total), 60)
        millis = int((total - int(total)) * 100)
        print(f"\n⏹️ Stopwatch stopped! Total Elapsed Time: {mins:02d}:{secs:02d}.{millis:02d}")

def main():
    print("=" * 45)
    print("⏱️ COUNTDOWN TIMER & STOPWATCH ⏱️".center(45))
    print("=" * 45)
    print("1. Countdown Timer")
    print("2. Stopwatch & Lap Tracker")
    print("3. Exit")

    choice = input("\nSelect Mode (1-3): ").strip()
    if choice == "1":
        countdown_timer()
    elif choice == "2":
        stopwatch()
    elif choice == "3":
        print("\nGoodbye! 👋\n")
    else:
        print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
