# Creating a Dictionary
my_dict = {
           "name": "John",            
           "age": 30, 
           "city": "New York"
           }
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


my_dict2 = dict(
    name="Alice", 
    age=25, 
    city="Los Angeles"
    )
print(my_dict2)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}

# explaining the difference between the two methods of creating a dictionary, 
# the first method uses curly braces {} and key-value pairs separated by colons, 
# while the second method uses the dict() constructor with keyword arguments. 
# Both methods create a dictionary, but the first method 
# is more commonly used and allows for more flexibility in defining keys and values.
# Moreover, the first method allows for keys to be of any immutable type (like strings, numbers, or tuples), while the second method requires keys to be valid Python identifiers (which means they must be strings that follow variable naming rules). 