# Age Eligibility Checker

person = input("Enter the Person Name: ").strip()
age = int(input("Enter the Age: "))
gender = input("Enter the Gender: ").strip().lower()

print()
print("Eligibility Report".center(40, "-"))

print(f"{'Name':<8}: {person}")
print(f"{'Age':<8}: {age}")
print(f"{'Gender':<8}: {gender.capitalize()}")

# Default Status
Voting_status = "❌ Not Eligible"
Driving_Status = "❌ Not Eligible"
Marriage_Status = "❌ Not Eligible"

if gender == "male":

    if age >= 18:
        print()
        print("Vote Eligible Status".center(40, "-"))
        print()
        print(f"Mr. {person} You are Eligible For Voting ✅")

        Voting_status = "✅ Eligible"

        print()
        print("Driving Licence Eligible Status".center(40, "-"))
        print()
        print(f"Mr. {person} You are Eligible For Driving Licence ✅")

        Driving_Status = "✅ Eligible"

        print()
        print("Marriage Eligible Status".center(40, "-"))
        print()

        if age >= 21:
            print(f"Mr. {person} You are Legally Eligible For Marriage ✅")
            Marriage_Status = "✅ Eligible"
        else:
            print(f"Mr. {person} You are Not Legally Eligible For Marriage ❌")

    else:
        print()
        print(f"Mr. {person} You are Not Eligible For Voting ❌")
        print(f"Mr. {person} You are Not Eligible For Driving Licence ❌")
        print(f"Mr. {person} You are Not Legally Eligible For Marriage ❌")

elif gender == "female":

    if age >= 18:
        print()
        print("Vote Eligible Status".center(40, "-"))
        print()
        print(f"Ms. {person} You are Eligible For Voting ✅")

        Voting_status = "✅ Eligible"

        print()
        print("Driving Licence Eligible Status".center(40, "-"))
        print()
        print(f"Ms. {person} You are Eligible For Driving Licence ✅")

        Driving_Status = "✅ Eligible"

        print()
        print("Marriage Eligible Status".center(40, "-"))
        print()

        # Marriage age for female
        print(f"Ms. {person} You are Legally Eligible For Marriage ✅")
        Marriage_Status = "✅ Eligible"

    else:
        print()
        print(f"Ms. {person} You are Not Eligible For Voting ❌")
        print(f"Ms. {person} You are Not Eligible For Driving Licence ❌")
        print(f"Ms. {person} You are Not Legally Eligible For Marriage ❌")

else:
    print()
    print("❌ Invalid Gender!")
    print("Please enter Male or Female.")
    exit()  # Exit the program because the input is invalid.
            # Prevents the Overall Summary from executing.
print()
print("-" * 35)
print("Overall Summary")
print("-" * 35)

print(f"{'Voting':<10}: {Voting_status}")
print(f"{'Driving':<10}: {Driving_Status}")
print(f"{'Marriage':<10}: {Marriage_Status}")

print("-" * 35)