# Default Input type is String

val = input("Enter anything: ")

print ("You entered: ", val)
print ("Data Type of the value: ", type(val))

print()
# Proper way to take input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

print ("Hello, ", name)
print ("Age: ", age)
print ("GPA: ", gpa)

print()
# Sum of two inputs

a = int(input("Enter 1st number: "))
b = float(input("Enter 2nd Number: "))

sum = a + b

print ("Sum of 2 inputs: ", sum)