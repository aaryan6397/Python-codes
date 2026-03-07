# Q1: Flatten a nested list into a single list
# Input: [[1, 2], [3, 4], [5, 6]]
# Output: [1, 2, 3, 4, 5, 6]

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Nested List:", nested_list)
print("Flattened List:", flat_list)

# Output:
# Nested List: [[1, 2], [3, 4], [5, 6]]
# Flattened List: [1, 2, 3, 4, 5, 6]