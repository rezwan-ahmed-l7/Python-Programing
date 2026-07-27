# If Else Statement

age = int(input("Enter age: "))

if(age >= 18):
    print("Adult")              # Indentation is important in Python
elif(age < 18 and age >= 0):
    print("Kid")
else:
    print("Invalid Number")

print()
# Nested If Else Statement

number = int(input("Enter Number: "))

if (number > 90):
    print("Grade A+")
elif(number > 80 & number < 90):
    print("Grade: A")
elif(number > 70 & number < 80):
    print("Grade: A-")
elif(number > 60 & number < 70):
    print("Grade: B+")
elif(number > 50 & number < 60):
    print("Grade: B")
elif(number > 40 & number < 50):
    print("Grade: B-")
elif(number > 30 & number < 40):
    print("Grade: C")
else:
    print("Fail")
