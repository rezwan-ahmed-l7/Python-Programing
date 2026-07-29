class Student:      # Class

    name = "Paris"
    age = 25

s1 = Student()      # Object
print(s1.name)
print(s1.age)

# Delete class attribute using del keyword
del s1.age 
print(s1.age)