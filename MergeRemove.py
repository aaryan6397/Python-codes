list1 = [10, 15, 30, 45, 60]
list2 = [15, 75, 90, 10, 120]

# Merge lists
merged = list1 + list2

# Remove duplicates
unique_list = list(set(merged))

# Sort in descending order
unique_list.sort(reverse=True)

print("Final List:", unique_list)

print("\nNumbers divisible by both 3 and 5:")

for num in unique_list:
    if num % 3 == 0 and num % 5 == 0:
        print(num)