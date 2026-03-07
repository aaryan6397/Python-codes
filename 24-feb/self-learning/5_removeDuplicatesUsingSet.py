# Q5: Remove duplicates from a list using a set and return a sorted list
# Input: [5, 3, 1, 2, 3, 5, 4, 1, 2]
# Output: [1, 2, 3, 4, 5]

numbers = [5, 3, 1, 2, 3, 5, 4, 1, 2]

unique_set = set(numbers)
sorted_list = sorted(unique_set)

print("Original List:", numbers)
print("After Removing Duplicates (Sorted):", sorted_list)

# Output:
# Original List: [5, 3, 1, 2, 3, 5, 4, 1, 2]
# After Removing Duplicates (Sorted): [1, 2, 3, 4, 5]