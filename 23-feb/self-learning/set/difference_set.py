# difference_set.py


# Take input for two sets 
set1 = set(input("Enter first set: ").split())
set2 = set(input("Enter second set: ").split())
# Find difference of the two sets using difference() method
result = set1.difference(set2)
# Print the difference of the sets
print("Difference (Set1 - Set2):", result)



'''output:
Enter first set: 1 2 3 4
Enter second set: 3 4 5 6
Difference (Set1 - Set2): {'1', '2'}
'''