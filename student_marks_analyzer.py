print("===== Student Marks Analyzer =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))
marathi = float(input("Enter Marathi marks: "))

total = maths + science + english + computer + marathi
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)