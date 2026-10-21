# Changing Items in a Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Changing the value of an existing key
my_dict["name"] = "Jane"
print(my_dict)  # Output: {'name': 'Jane', 'age': 30, 'city': 'New York'}

# Adding a new key-value pair
my_dict["height"] = 175
print(my_dict)  # Output: {'name': 'Jane', 'age': 30, 'city': 'New York', 'height': 175}

# Removing a key-value pair
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Jane', 'city': 'New York', 'height': 175}          


# Removing a key-value pair using the pop() method
removed_value = my_dict.pop("city")
print(removed_value)  # Output: New York
print(my_dict)  # Output: {'name': 'Jane', 'height': 175}       