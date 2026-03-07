# Problem 83
# Problem Statement: Check whether key exists in dictionary.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of items : "))
my_dict = {}
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    my_dict[key] = value

print("Dictionary :", my_dict)

search_key = input("Enter key to search : ")

if search_key in my_dict:
    print("Key", search_key, "exists in the dictionary with value :", my_dict[search_key])
else:
    print("Key", search_key, "does not exist in the dictionary")

# output
# Enter number of items : 3
# Enter key : name
# Enter value : Anshul
# Enter key : age
# Enter value : 21
# Enter key : city
# Enter value : Delhi
# Dictionary : {'name': 'Anshul', 'age': '21', 'city': 'Delhi'}
# Enter key to search : age
# Key age exists in the dictionary with value : 21
