# 🏋️ Day 03: BMI (Body Mass Index) Calculator

A beginner-friendly Python program to compute Body Mass Index (BMI), classify nutritional status according to WHO health categories, and provide healthy lifestyle recommendations.

---

## 📌 Concepts Covered
- Standard user input (`input()`) and string sanitization (`.strip()`, `.title()`).
- Data type conversion and validation (`float()`, `try-except ValueError`).
- Mathematical operations (Power `**`, Division `/`, `round()`).
- Multi-branch conditional logic (`if`, `elif`, `else`).
- Clean ASCII formatted report generation.

---

## 🧮 BMI Formula
$$\text{BMI} = \frac{\text{Weight in kg}}{(\text{Height in meters})^2}$$

### Standard Categories:
| BMI Range | Category |
|---|---|
| `< 18.5` | Underweight |
| `18.5 – 24.9` | Normal / Healthy Weight |
| `25.0 – 29.9` | Overweight |
| `≥ 30.0` | Obese |

---

## 🚀 How to Run

```bash
python 03_BMI_Calculator.py
```

---

## 📋 Sample Output

```text
========================================
             BMI CALCULATOR             
========================================
Enter your Name: Rahul
Enter your Height in meters (e.g. 1.75): 1.72
Enter your Weight in kg (e.g. 68.5): 65.0

----------------------------------------
           BMI HEALTH REPORT            
----------------------------------------
Name        : Rahul
Height      : 1.72 m
Weight      : 65.0 kg
BMI Score   : 21.97
Category    : Normal / Healthy Weight ✅
Advice      : Great job! Keep maintaining a balanced diet and regular exercise.
----------------------------------------
```
