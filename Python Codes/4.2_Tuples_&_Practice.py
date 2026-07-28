# Tuples 

tup = (1, 2, 3, 4, 5)

print(tup)
print(tup[2])

print()
# Tuple Slicing

tup1 = (1, 2, 3, 4, 5)
result = tup1[1:5]

print(result)

print()
# Tuple Methods

tup2 = (2, 4, 6, 8, 10)

print(tup2.count(2))  # Returns the number of occurrences of a specified value in a tuple
print(tup2.index(6))  # Returns the index of the first occurrence of a specified value in a tuple

print()
# Practice

# Take 3 input and store in list

numbers = [ ]

numbers.append(int(input("1st Number: ")))
numbers.append(int(input("2nd Number: ")))
numbers.append(int(input("3rd Number: ")))

print("Numbers are: ",numbers)

print()
# Palindrome

list = [1, 2, 3, 2, 1]

list2 = list.copy()
list2.reverse()

if(list2 == list):
    print("Palindrome")
else:
    print("Not Palindrome")

print()
# Swap

list3 = [1, 2, 3, 4, 5]
list3[0], list3[4] = list3[4], list3[0]

print(list3)

print()
# Count A in tuple

grade = ("A", "B", "A", "D", "A", "B", "D", "C")
print(grade.count("A"))

print()
# Sort A to E in tuple

letter = ["A", "B", "A", "D", "A", "B", "D", "C"]
letter.sort()

print(letter)