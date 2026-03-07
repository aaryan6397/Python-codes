# Q7: Group list elements by their data type using a dictionary
# Input: [1, "hello", 2.5, "world", 3, 4.0, "python"]
# Output: {'int': [1, 3], 'str': ['hello', 'world', 'python'], 'float': [2.5, 4.0]}

mixed_list = [1, "hello", 2.5, "world", 3, 4.0, "python"]

grouped = {}
for item in mixed_list:
    type_name = type(item).__name__
    if type_name in grouped:
        grouped[type_name].append(item)
    else:
        grouped[type_name] = [item]

print("Mixed List:", mixed_list)
print("Grouped by Type:", grouped)

# Output:
# Mixed List: [1, 'hello', 2.5, 'world', 3, 4.0, 'python']
# Grouped by Type: {'int': [1, 3], 'str': ['hello', 'world', 'python'], 'float': [2.5, 4.0]}