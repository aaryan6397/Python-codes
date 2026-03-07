# dict_add_module.py
#  Function to add a key-value pair in dictionary

def add_item(d, key, value):
    # Add new item to dictionary
    d[key] = value
    
    # Return updated dictionary
    return d




# dict_create_module.py
#  Function to create and return a dictionary

def create_dict():
    # Creating dictionary with student data
    student = {
        "name": "Rahul",
        "age": 20,
        "course": "BCA"
    }
    
    # Return dictionary
    return student




# dict_delete_module.py
#  Function to delete key from dictionary

def delete_item(d, key):
    
    # Check if key exists
    if key in d:
        del d[key]   # delete key-value pair
    
    return d




# dict_search_module.py
# Function to search key in dictionary

def search_key(d, key):
    
    # Check if key exists
    if key in d:
        return "Key found"
    else:
        return "Key not found"
    



    # dict_update_module.py
#Function to update dictionary value

def update_value(d, key, value):
    # Update the value for given key
    d[key] = value
    
    return d
