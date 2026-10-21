# Copying a Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using the copy() method
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Using the dict() constructor
new_dict = dict(my_dict)
print(new_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}  