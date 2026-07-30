# String Slicing

e = "Hello World"
slice1 = e[0:5]  # Slicing from index 0 to 4 (5 is exclusive)
slice2 = e[6:]   # Slicing from index 6 to the end of the string

print("Index 0 to 4: ", slice1)
print("Index 6 to the end: ", slice2)
print(e[2:7])   # Slicing from index 2 to 6 (7 is exclusive)

print()
# String Slicing with Negative Indexing
slice3 = e[-5:]  # Slicing the last 5 characters of the string
slice4 = e[:-6]  # Slicing from the start to the 6th last character

print("Last 5 characters: ", slice3)
print("From start to 6th last character: ", slice4)
print(e[-8:-3])  # Last 3 characters

print()
# String Reverse

str = "Hello World"
reverse_str = str[::-1]  # Reversing the string using slicing

print("Reversed string is: ", reverse_str)
print(str[::-1])  # Reversing the string using slicing
