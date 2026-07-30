# Length of a string

name = input("Enter your name: ")
length = len(name)

print ("Length of string: ", length)
print(len(name))

print()
# Count " I " in the string

str = "I am Paris. I am a student. I love programming."
count = str.count("I")

print ("Count of 'I' in the string: ", count)
print(str.count("I"))

print()
# String Reverse

ans = input("Enter a sentence: ")
reverse = ans[::-1]

print("Reversed: ", reverse)
print(ans[::-1])

print()
# String Concatenation

greeting = input("Enter greeting: ")
names = input("Enter names: ")

result = greeting + " " + names

print("Joint result: ", result)
print(greeting + " " + names)