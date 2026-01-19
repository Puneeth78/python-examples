# # 1️⃣ Create and Print a Dictionary

# # Question: Create a dictionary students with keys "puneeth", "rama", "sita" and values 35, 45, 52. Print it.

students = {
    "puneeth": 35,
    "rama": 45,
    "sita": 52
}
print(students)


# # Output:

# {'puneeth': 35, 'rama': 45, 'sita': 52}

# 2️⃣ Access Keys and Values

# Question: Print all keys and values of the dictionary.

print(students.keys())
print(students.values())


# Output:

# dict_keys(['puneeth', 'rama', 'sita'])
# dict_values([35, 45, 52])

# 3️⃣ Check if a Key Exists

# Question: Check if "puneeth" exists in the dictionary.

if "puneeth" in students:
    print("yes")
else:
    print("no")


# Output:

# yes

# 4️⃣ Delete a Key

# Question: Delete "puneeth" from the dictionary.

del students["puneeth"]
print(students)


# Output:

# {'rama': 45, 'sita': 52}

# 5️⃣ Update Values

# Question: Update the dictionary with new values.

students.update({"puneeth":12, "rama":15, "sita":23})
print(students)


# Output:

# {'puneeth': 12, 'rama': 15, 'sita': 23}

# 6️⃣ Add a New Key

# Question: Add a new key "age" with value 21. Print the updated dictionary.

students["age"] = 21
print(students)


# Output:

# {'puneeth': 12, 'rama': 15, 'sita': 23, 'age': 21}

# 7️⃣ Get Items as Tuples

# Question: Print all dictionary items (key-value pairs) as tuples.

print(students.items())


# Output:

# dict_items([('puneeth', 12), ('c 15), ('sita', 23), ('age', 21)])

# 8️⃣ Create Dictionary from Two Lic

# Question: Create a dictionary uceys = ["a","b","c"] and values = [1,2,3].

keys = ["a", "b", "c"]
values = [1, 2, 3]
result = dict(zip(keys, values))
print(result)


# Output:

# {'a': 1, 'b': 2, 'c': 3}

# 9️⃣ Find the Topper (Maximum Valuc

# Question: Find the student withcighest marks.

students = {
    "puneeth": 35,
    "anjana": 45,
    "vandana": 52
}
topper = max(students, key=students.get)
print(topper, students[topper])


# Output:

# vandana 52