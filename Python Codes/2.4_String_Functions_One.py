# str.endswith(" ")

a = "Hello World"
result1 = a.endswith("World")

print(result1)  # Returns True if the string ends with the specified suffix, otherwise False
print(a.endswith("Hello"))  # Returns False

print()


# str.startswith(" ")

b = "Hello World"
result2 = b.startswith("Hello")

print(result2)  # Returns True if the string starts with the specified prefix, otherwise False
print(b.startswith("World"))  # Returns False

print()


# str.capitalize()

c = "hello world"
result3 = c.capitalize()

print(result3)  # Returns a copy of the string with the first character capitalized and the rest lowercase
print(c.capitalize())  # Returns "Hello world"
print(c)  # Original string remains unchanged
