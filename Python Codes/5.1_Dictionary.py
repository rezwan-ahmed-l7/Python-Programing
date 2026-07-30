info = {
    "name" : "Paris",
    "age" : 25,
    "gpa" : 3.5,
    "adult" : True,
    "subject" : ["DSA", "OOP", "DBMS"],
    "topics" : { "Dictionary", "Sets"},
}

print(info)
print(info["name"])

print()
info["name"] = "Rezwan" # Overwriting
info["address"] = "Dhaka"
print(info)

print()
print(info.keys()) # Returns the keys of the dictionary
print(info.values()) # Returns the values of the dictionary
print(info.items()) # Returns the key-value pairs of the dictionary

info2 = {"city" : "Dhaka"}
info.update(info2) # Updating value
print(info)