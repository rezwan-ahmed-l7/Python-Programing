# List (Array) in Python

marks = [90, 80, 70, 60, 50, 40, 30]

print(marks)
print(marks[4]) # Accessing fifth element
print(len(marks))  # Length of the list

student = ["Paris", 25, 3.5, "Dhaka"]

print (student)
print(student[3])

student[1] = 26  # Changing the value of an element
print(student)

# List Slicing

marks2 = [95, 85, 75, 65, 55, 45, 35]
result = marks2[2:5]  # Accessing elements from index 2 to 4

print(result)  # Accessing elements from index 1 to 3
print(marks2[1:4])  # Accessing elements from index 0 to 3

# List Reverse

marks3 = [99, 77, 66, 88, 55, 44, 33]

marks3.reverse()  # Reversing the list
print(marks3)