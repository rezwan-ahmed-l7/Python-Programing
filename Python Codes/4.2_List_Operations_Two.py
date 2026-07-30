# List Methods

teacher = ["Ryn", 35, 4.0, "Male"]

teacher.append("Male")  # Adding a new element at end
print(teacher)

teacher.insert(1, "Female")  # Adding a new element (index, Value)
print(teacher)

teacher.remove("Male")  # Removing an element
print(teacher)

teacher.pop()  # Removing the last element
print(teacher)

print()
teacher2 = [93, 83, 56, 29, 72, 65, 38]
teacher3 = ["Arian", "Safal", "Rizen", "Blake"]

teacher2.sort()  # Sorting the list in ascending order
teacher3.sort()
print(teacher2)
print(teacher3)

teacher2.sort(reverse=True) # Descending order
teacher3.sort(reverse=True)
print(teacher2)
print(teacher3)