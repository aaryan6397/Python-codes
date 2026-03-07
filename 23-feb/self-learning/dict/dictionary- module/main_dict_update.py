# main_dict_update.py

import dict_multiple_module

# Create dictionary
data = {"name": "Ravi", "age": 22}

# Update age
result = dict_multiple_module.update_value(data, "age", 23)

# Print result
print("Updated Dictionary:", result)



'''output:
Updated Dictionary: {'name': 'Ravi', 'age': 23}

'''