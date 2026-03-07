# Q4: Find the union and intersection of two sets
# Input: set1 = {10, 20, 30, 40}, set2 = {30, 40, 50, 60}
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {30, 40}


# Define the two sets
set1 = {10, 20, 30, 40}

set2 = {30, 40, 50, 60}

# Find union and intersection of the two sets
union_set = set1.union(set2)
# Find intersection of the two sets using intersection() method
intersection_set = set1.intersection(set2)

# Print the sets, union and intersection
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)

# Output:
# Set 1: {40, 10, 20, 30}
# Set 2: {40, 50, 60, 30}
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {40, 30}