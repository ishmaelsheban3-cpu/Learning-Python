# Membership Operators - used to test if a sequence is presented in an object       
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("mango" not in fruits)  # Output: True

# Another example:
text = "Hello, World!"
print("Hello" in text)  # Output: True
print("Python" not in text)  # Output: True

# More examples with sets:
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # Output: True
print(6 not in numbers)  # Output: True

# More examples with dictionaries:
person = {"name": "Alice", "age": 30, "city": "New York"}
print("name" in person)  # Output: True 
print("age" in person)   # Output: True
print("country" not in person)  # Output: True