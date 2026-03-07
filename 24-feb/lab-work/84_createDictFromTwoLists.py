# Problem 84
# Problem Statement: Create dictionary from two lists.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of elements : "))

keys = []
print("Enter keys :")
for i in range(n):
    key = input("Enter key : ")
    keys.append(key)

values = []
print("Enter values :")
for i in range(n):
    value = input("Enter value : ")
    values.append(value)

my_dict = {}
for i in range(n):
    my_dict[keys[i]] = values[i]

print("Keys list :", keys)
print("Values list :", values)
print("Created dictionary :", my_dict)

# output
# Enter number of elements : 3
# Enter keys :
# Enter key : name
# Enter key : age
# Enter key : city
# Enter values :
# Enter value : Anshul
# Enter value : 21
# Enter value : Delhi
# Keys list : ['name', 'age', 'city']
# Values list : ['Anshul', '21', 'Delhi']
# Created dictionary : {'name': 'Anshul', 'age': '21', 'city': 'Delhi'}