# 2.⁠ ⁠Grade Calculator
# Input:
# Student name
# 5 marks
# Output:
# Total
# Percentage
# Grade (A/B/C/D/F)
grade = ''
result_status = ''
name = input("Enter the Student Name: ")
if not name.isalpha():
    print("❌ Invalid Name! Please Enter Only Alphabets")
    exit()
else:

    sub1 = int(input("Enter the Marks: "))
    sub2 = int(input("Enter the Marks: "))
    sub3 = int(input("Enter the Marks: "))
    sub4 = int(input("Enter the Marks: "))
    sub5 = int(input("Enter the Marks: "))

# Input Validation
if (
    0 <= sub1 <= 100 and
    0 <= sub2 <= 100 and
    0 <= sub3 <= 100 and
    0 <= sub4 <= 100 and
    0 <= sub5 <= 100
):

    # Total Marks Calculation
    total_marks = sub1 + sub2 + sub3 + sub4 + sub5
    # Percentage Calculation
    percentage = total_marks / 5

else:
    print("❌ Invalid Marks! Please enter marks between 0 and 100.")
    exit()

if  percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 35:
    grade = 'E'
else:
    grade = 'F'
if percentage >= 35:
    result_status = 'Pass'
else:
    result_status = 'Fail'

print("Marks Card".center(35,'-'))
print(f"Student Name: {name}")
print(f"Total_Marks : {total_marks}")
print(f"Percentage  : {percentage}")
print(f"Grade       : {grade}")
print(f"Result      : {result_status}")
print('-' * 35)