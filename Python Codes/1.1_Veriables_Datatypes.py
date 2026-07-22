""" Variables and Datatypes """ # Multi-line Comment

name = "Paris"
age = 25
gpa = 3.50
Human = True
pets = None

print ("My name is: ", name)
print ("My age is: ", age)
print ("My GPA is: ", gpa)
print ("Am I a human? ", Human)
print ("Do I have pets? ", pets)

print()
# Data Type of variables
print ("Data Type of variables")

print (type(name))
print (type(age))
print (type(gpa))
print (type(Human))
print (type(pets))

print()
# Type Conversion
print ("Type Conversion")

a = 5
b = 10.5

sum = a + b

print ("Sum: ", sum)

print()
# Type Casting
print ("Type Casting")

c = 5
d = float(c)

print (type(d))

e = 10.5
f = int(e)

print (type(f))

g = "15"
h = int(g)

print (type(h))

i = 20
j = str(i)
print (type(j))