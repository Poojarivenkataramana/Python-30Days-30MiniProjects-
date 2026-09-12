# ----------------------------------------------------
# Day 06: Universal Unit Converter
# Concepts: Functions, Dictionaries, Mathematical Conversions, Modular Design
# ----------------------------------------------------

def convert_temperature(value, from_u, to_u):
    # Convert input to Celsius first
    if from_u == "c":
        celsius = value
    elif from_u == "f":
        celsius = (value - 32) * 5 / 9
    elif from_u == "k":
        celsius = value - 273.15
    else:
        return None

    # Convert Celsius to target
    if to_u == "c":
        return celsius
    elif to_u == "f":
        return (celsius * 9 / 5) + 32
    elif to_u == "k":
        return celsius + 273.15
    return None

def convert_length(value, from_u, to_u):
    # Base unit: Meter
    factors = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }
    if from_u in factors and to_u in factors:
        meters = value * factors[from_u]
        return meters / factors[to_u]
    return None

def convert_weight(value, from_u, to_u):
    # Base unit: Kilogram
    factors = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    if from_u in factors and to_u in factors:
        kg = value * factors[from_u]
        return kg / factors[to_u]
    return None

def main():
    print("=" * 45)
    print("🔄 UNIVERSAL UNIT CONVERTER 🔄".center(45))
    print("=" * 45)

    while True:
        print("\nSelect Category:")
        print("1. Temperature (C, F, K)")
        print("2. Length (m, km, cm, mm, mile, yard, foot, inch)")
        print("3. Weight (kg, g, mg, lb, oz)")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()
        if choice == "4":
            print("\nThank you for using Universal Unit Converter! Goodbye 👋\n")
            break

        if choice not in ("1", "2", "3"):
            print("❌ Invalid option! Please select 1, 2, 3, or 4.")
            continue

        try:
            val = float(input("\nEnter the value to convert: "))
        except ValueError:
            print("❌ Invalid number!")
            continue

        if choice == "1":
            print("Units: C (Celsius), F (Fahrenheit), K (Kelvin)")
            from_u = input("From Unit: ").strip().lower()
            to_u = input("To Unit: ").strip().lower()
            res = convert_temperature(val, from_u, to_u)
        elif choice == "2":
            print("Units: m, km, cm, mm, mile, yard, foot, inch")
            from_u = input("From Unit: ").strip().lower()
            to_u = input("To Unit: ").strip().lower()
            res = convert_length(val, from_u, to_u)
        elif choice == "3":
            print("Units: kg, g, mg, lb, oz")
            from_u = input("From Unit: ").strip().lower()
            to_u = input("To Unit: ").strip().lower()
            res = convert_weight(val, from_u, to_u)

        if res is not None:
            print("\n" + "-" * 45)
            print(f"✅ Result: {val} {from_u.upper()} = {round(res, 4)} {to_u.upper()}")
            print("-" * 45)
        else:
            print("❌ Invalid unit codes provided. Please try again.")

if __name__ == "__main__":
    main()
