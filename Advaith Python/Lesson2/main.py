str1 = "Hello"
str2 = "World"
combined = str1 + "" + str2
print("Concentrated string:", combined)

repeated = str1 * 3
print("Repeated string:", repeated)

slice_str = combined[0:5]
print("Sliced string:", slice_str)

upper_str = str1.upper()
print("Upper case string:",upper_str)

lower_str = str2.lower()
print("Lower case string:",lower_str)

print("lenght of combiened string:", len(combined))


num_str = "15"
num_from_str = int(num_str)
print("String to intiger:",num_from_str)
