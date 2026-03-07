# Problem 80
# Problem Statement: Sort dictionary by values.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of items : "))
my_dict = {}
for i in range(n):
    key = input("Enter key : ")
    value = int(input("Enter value : "))
    my_dict[key] = value

print("Original dictionary :", my_dict)

sorted_keys = []
sorted_values = sorted(my_dict.values())
sorted_dict = {}

for val in sorted_values:
    for key in my_dict:
        if my_dict[key] == val and key not in sorted_keys:
            sorted_dict[key] = val
            sorted_keys.append(key)
            break

print("Dictionary sorted by values :", sorted_dict)

# output
# Enter number of items : 4
# Enter key : banana
# Enter value : 3
# Enter key : apple
# Enter value : 1
# Enter key : cherry
# Enter value : 4
# Enter key : date
# Enter value : 2
# Original dictionary : {'banana': 3, 'apple': 1, 'cherry': 4, 'date': 2}
# Dictionary sorted by values : {'apple': 1, 'date': 2, 'banana': 3, 'cherry': 4}