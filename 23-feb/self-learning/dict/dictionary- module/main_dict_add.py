# main_dict_add.py

import dict_multiple_module

# Initial dictionary
data = {"name": "Amit", "age": 21}

# Add new item using module function
result = dict_multiple_module.add_item(data, "course", "BCA")

# Print updated dictionary
print("Updated Dictionary:", result)


'''output:
Updated Dictionary: {'name': 'Amit', 'age': 21, 'course': 'BCA'}

'''



