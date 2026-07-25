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

print()
# str.replace("old", "new")

d = "Hello World"
result4 = d.replace("World", "Universe")

print(result4)  # Returns a copy of the string with all occurrences of the old substring replaced by the new substring
print(d.replace("Hello", "Hi"))  # Returns "Hi World"

print()
# str.find("substring")

e = "Hi everyone, im a student of BAUST"
result5 = e.find("student")

print(result5)  # Returns the lowest index of the substring if found, otherwise -1
print(e.find("teacher"))  # Returns -1 since "teacher" is not found in the string

print()
# str.count("substring")

f = "Hello World, Hello Universe"
result6 = f.count("Hello")

print(result6)  # Returns the number of non-overlapping occurrences of the substring in the string
print(f.count("Hi"))  # Returns 0 since "Hi" is not found in