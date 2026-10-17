# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']

# Explanation:
# In this code snippet, we define a list called 'fruits' that contains five string elements.
# We then use list comprehension to create a new list called 'newlist' that contains only the 
# fruits that have the letter "a" in their name.
# Finally, we print the new list.   