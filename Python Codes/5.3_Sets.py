sets = {1, 2, "Apple", 4, "Mango", 6, "Banana", 3}

print(sets)
print(type(sets))

print()
# Empty set

box = set()

print(type(box))

print()
# Set Methods

basket = set()

basket.add("apple")
basket.add("mango")
basket.add("banana")
basket.add("orange")
print(basket)

basket.remove("mango")
print(basket)

basket.pop()
print(basket)

basket.clear()
print(basket)

# Union and Intersection

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1.union(s2))
print(s1.intersection(s2))
