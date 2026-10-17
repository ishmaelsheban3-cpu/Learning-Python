# Join Two Lists
list1 = ["apple", "banana", "cherry"]
list2 = ["date", "elderberry", "fig"]
joined_list = list1 + list2
print(joined_list)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Explanation:
# In this code snippet, we define two lists called 'list1' and 'list2' that contain string elements.
# We then use the '+' operator to join the two lists into a new list called 'joined_list'.
# Finally, we print the joined list.

# Extend a List
list1 = ["apple", "banana", "cherry"]
list2 = ["date", "elderberry", "fig"]
list1.extend(list2)
print(list1)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Explanation:
# In this code snippet, we define two lists called 'list1' and 'list2' that contain string elements.
# We then use the extend() method to add all elements from 'list2' to 'list1'.
# Finally, we print the extended list.