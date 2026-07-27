# If number is even or odd

number = int(input("Enter Number: "))

if(number % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")

print()
# Greatest of Three Numbers

n1 = int(input("1st Number: "))
n2 = int(input("2nd Number: "))
n3 = int(input("3rd Number: "))

if(n1 > n2 and n1 > n3):
    print("1st Number is Greatest")
elif(n2 > n1 and n2 > n3):
    print("2nd Number is Greatest")
else:
    print("3rd Number is Greatest")

print()
