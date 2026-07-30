## Area of square, rectangle and triangle

hight = float(input("Enter hight: "))
width = float(input("Enter width: "))

square = hight * hight
rectangle = hight * width
triangle = 0.5 * hight * width

print ("Area of square: ", square)
print ("Area of rectangle: ", rectangle)
print ("Area of triangle: ", triangle)

print()
# Average of 3 numbers

a = int(input("1st number: "))
b = float(input("2nd number: "))
c = int(input("3rd number: "))

average = (a + b + c) / 3

print ("Average of 3 numbers: ", average)

print()
# True False

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

print ("Is a equal to b? ", a == b)
print ("Is a not equal to b? ", a != b)
print ("Is a greater than b? ", a > b)
print ("Is a less than b? ", a < b)