# ----------------------------------------------------
# Day 21: CLI Alarm Clock with Snooze Functionality
# Concepts: datetime module, time.sleep(), string parsing, alert triggers
# ----------------------------------------------------

from datetime import datetime, timedelta
import time
import sys

def trigger_alarm(message):
    print("\n" + "🔔" * 20)
    print(f"⏰ ALARM RINGING! {message} ⏰".center(40))
    print("🔔" * 20)

    # Ring bell 5 times
    for _ in range(5):
        print("\a", end="", flush=True)
        time.sleep(0.5)

    while True:
        action = input("\nOptions: [D]ismiss or [S]nooze 5 minutes: ").strip().lower()
        if action in ("d", "dismiss"):
            print("✅ Alarm dismissed. Have a great day!")
            return None
        elif action in ("s", "snooze"):
            snooze_time = datetime.now() + timedelta(minutes=5)
            print(f"💤 Snoozing for 5 minutes. New alarm set for: {snooze_time.strftime('%H:%M:%S')}")
            return snooze_time
        else:
            print("❌ Invalid option. Enter 'D' or 'S'.")

def start_alarm(alarm_dt, message):
    print(f"\n⏳ Alarm armed for {alarm_dt.strftime('%H:%M:%S')}. Monitoring time...")
    print("Press Ctrl+C to cancel alarm at any time.\n")

    try:
        while True:
            now = datetime.now()
            remaining = (alarm_dt - now).total_seconds()

            if remaining <= 0:
                new_dt = trigger_alarm(message)
                if new_dt:
                    alarm_dt = new_dt
                else:
                    break
            else:
                mins, secs = divmod(int(remaining), 60)
                hours, mins = divmod(mins, 60)
                print(f"\rCurrent Time: {now.strftime('%H:%M:%S')} | ⏳ Remaining: {hours:02d}:{mins:02d}:{secs:02d} ", end="", flush=True)
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n⏹️ Alarm cancelled by user.")

def main():
    print("=" * 45)
    print("⏰ SMART CLI ALARM CLOCK ⏰".center(45))
    print("=" * 45)

    print(f"Current System Time: {datetime.now().strftime('%H:%M:%S')}\n")

    while True:
        alarm_input = input("Enter alarm time (Format HH:MM:SS or HH:MM): ").strip()
        try:
            parts = [int(p) for p in alarm_input.split(":")]
            if len(parts) == 2:
                h, m = parts
                s = 0
            elif len(parts) == 3:
                h, m, s = parts
            else:
                raise ValueError

            if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
                print("❌ Hours must be 0-23, Minutes 0-59, Seconds 0-59.")
                continue
            break
        except ValueError:
            print("❌ Invalid format! Please enter time like '18:30' or '07:15:00'.")

    message = input("Enter custom alarm label/note (e.g. 'Meeting', 'Workout'): ").strip()
    if not message:
        message = "Wake Up!"

    now = datetime.now()
    alarm_dt = now.replace(hour=h, minute=m, second=s, microsecond=0)

    # If the time is in the past for today, set it for tomorrow
    if alarm_dt <= now:
        alarm_dt += timedelta(days=1)
        print(f"ℹ️ Specified time has already passed today; setting alarm for tomorrow at {alarm_dt.strftime('%Y-%m-%d %H:%M:%S')}.")

    start_alarm(alarm_dt, message)

if __name__ == "__main__":
    main()
