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