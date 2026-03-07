# Q8: Swap keys and values of a dictionary
# Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}

original = {"a": 1, "b": 2, "c": 3}

swapped = {}
for key, value in original.items():
    swapped[value] = key

print("Original Dict:", original)
print("Swapped Dict:", swapped)

# Output:
# Original Dict: {'a': 1, 'b': 2, 'c': 3}
# Swapped Dict: {1: 'a', 2: 'b', 3: 'c'}