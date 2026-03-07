# main_dict_delete.py

import dict_multiple_module

# Sample dictionary
data = {"name": "Sita", "age": 19, "course": "BCA"}

# Delete age key
result = dict_multiple_module.delete_item(data, "age")

# Print dictionary
print("Dictionary after deletion:", result)


'''output:
Dictionary after deletion: {'name': 'Sita', 'course': 'BCA'}

'''