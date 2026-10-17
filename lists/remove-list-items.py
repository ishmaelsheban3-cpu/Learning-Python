# Remove List Items
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
my_list.remove("banana")  # This will raise a ValueError since "banana" is no longer in the list  
my_list.remove("apple")       
print(my_list)  # Output: ['cherry']

# Explanation:
# In this code snippet, we define a list called 'my_list' that contains three string elements.
# We then remove the element "banana" from the list using the remove() method.
# Finally, we print the updated list.       