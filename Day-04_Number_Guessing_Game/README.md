# 🎯 Day 04: Number Guessing Game

An interactive console-based game where the computer picks a random secret number between 1 and 100, and the player tries to guess it within a limited number of attempts based on the chosen difficulty level.

---

## 📌 Concepts Covered
- `random.randint()` for pseudo-random number generation.
- `while` loops for turn-based gameplay.
- Input validation (`isdigit()`, range checking).
- Dynamic hints (Hot/Cold feedback based on proximity).
- Replay game loop architecture.

---

## 🎮 Features
- **3 Difficulty Levels**: Easy (10 attempts), Medium (7 attempts), Hard (5 attempts).
- **Interactive Proximity Hints**: Tells the player if they are "Too High", "Too Low", or "Very Close".
- **Attempt Tracking**: Shows remaining attempts before game over.
- **Play Again Loop**: Allows seamless replaying without restarting the script.

---

## 🚀 How to Run

```bash
python 04_Number_Guessing_Game.py
```
