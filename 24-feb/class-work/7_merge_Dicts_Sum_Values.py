# Q7: Merge two dictionaries and sum values of common keys
# Input: dict1 = {"a": 5, "b": 10, "c": 3}, dict2 = {"b": 7, "c": 2, "d": 8}
# Output: {"a": 5, "b": 17, "c": 5, "d": 8}


# Define the two dictionaries
dict1 = {"a": 5, "b": 10, "c": 3}
dict2 = {"b": 7, "c": 2, "d": 8}
# Create a new dictionary to store merged results
merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
# Print the original dictionaries and the merged result
print("Dict 1:", dict1)
# print("Dict 2:", dict2) --- IGNORE ---
print("Dict 2:", dict2)
# print("Merged Dict:", merged) --- IGNORE ---
print("Merged Dict:", merged)

# Output:
# Dict 1: {'a': 5, 'b': 10, 'c': 3}
# Dict 2: {'b': 7, 'c': 2, 'd': 8}
# Merged Dict: {'a': 5, 'b': 17, 'c': 5, 'd': 8}