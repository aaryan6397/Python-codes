# Q2: Convert two lists into a dictionary
# Input: keys = ["name", "age", "city"], values = ["Anshul", 21, "Delhi"]
# Output: {"name": "Anshul", "age": 21, "city": "Delhi"}

keys = ["name", "age", "city"]
values = ["Anshul", 21, "Delhi"]

result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print("Keys:", keys)
print("Values:", values)
print("Dictionary:", result)

# Output:
# Keys: ['name', 'age', 'city']
# Values: ['Anshul', 21, 'Delhi']
# Dictionary: {'name': 'Anshul', 'age': 21, 'city': 'Delhi'}