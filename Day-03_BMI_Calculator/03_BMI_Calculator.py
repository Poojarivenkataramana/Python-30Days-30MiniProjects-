# ----------------------------------------------------
# Day 03: BMI (Body Mass Index) Calculator
# Concepts: User Input, Type Casting, Arithmetic Operators, Conditional Statements (if-elif-else)
# ----------------------------------------------------

print("=" * 40)
print("BMI CALCULATOR".center(40))
print("=" * 40)

# Input: Name validation
name = input("Enter your Name: ").strip()
if not name.replace(" ", "").isalpha():
    print("❌ Invalid Name! Please enter alphabetic characters only.")
    exit()

# Input: Height validation (in meters)
try:
    height = float(input("Enter your Height in meters (e.g. 1.75): "))
    if height <= 0 or height > 2.7:
        print("❌ Invalid Height! Please enter a realistic height between 0.1m and 2.7m.")
        exit()
except ValueError:
    print("❌ Invalid input! Height must be a numeric value.")
    exit()

# Input: Weight validation (in kilograms)
try:
    weight = float(input("Enter your Weight in kg (e.g. 68.5): "))
    if weight <= 0 or weight > 500:
        print("❌ Invalid Weight! Please enter a realistic weight between 1kg and 500kg.")
        exit()
except ValueError:
    print("❌ Invalid input! Weight must be a numeric value.")
    exit()

# BMI Formula: weight (kg) / (height (m) ^ 2)
bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)

# Categorization based on WHO BMI Standards
if bmi < 18.5:
    category = "Underweight"
    advice = "Consider a nutrient-rich diet to reach a healthy weight."
elif 18.5 <= bmi < 25:
    category = "Normal / Healthy Weight ✅"
    advice = "Great job! Keep maintaining a balanced diet and regular exercise."
elif 25 <= bmi < 30:
    category = "Overweight"
    advice = "Consider adopting regular physical activity and a balanced diet."
else:
    category = "Obese"
    advice = "Consult a healthcare professional for personalized guidance."

# Output Summary Card
print()
print("-" * 40)
print("BMI HEALTH REPORT".center(40))
print("-" * 40)
print(f"{'Name':<12}: {name.title()}")
print(f"{'Height':<12}: {height} m")
print(f"{'Weight':<12}: {weight} kg")
print(f"{'BMI Score':<12}: {bmi_rounded}")
print(f"{'Category':<12}: {category}")
print(f"{'Advice':<12}: {advice}")
print("-" * 40)
