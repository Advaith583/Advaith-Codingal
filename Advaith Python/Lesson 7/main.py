# fruits = ["apple","banana","cherry"]
# print("Orignial list:",fruits)

# fruits.append("mango")
# print("After appending 'mango':", fruits)


# fruits.remove("banana")
# print("After removing 'banana':", fruits)


# print("first element of the list:", fruits[0])

# print("Iterating through the list:")


# for x in fruits:
#     print(x)

student = {
    "name": "Faiq",
    "age": 15,
    "grade": "10th"
}

print("Original dictionary:", student)

print("Name of the student:", student["name"])

student["school"] = "ABC High School"
print("After updating 'school':",student)

student["age"] = 16
print("after updating 'age':", student)

del student["grade"]
print("After deleting 'grade':", student)

print("Iterating through the dictionary:")
for key, value in student.items():
    print(key,":", value)