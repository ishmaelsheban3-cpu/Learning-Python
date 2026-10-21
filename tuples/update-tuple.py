# Updating Tuple Elements
# Tuples are immutable, so you cannot update elements directly.
# However, you can create a new tuple with the desired changes.

# example
sample_tuple = (1, 2, 3, 4, 5)

# Creating a new tuple with an updated element
new_tuple = sample_tuple[:2] + (10,) + sample_tuple[3:]

# explaining the code
# In this example, we create a new tuple called new_tuple.
# The slicing operation sample_tuple[:2] gets the first two elements.
# The tuple (10,) contains the new value we want to insert.
# The slicing operation sample_tuple[3:] gets the elements from index 3 to the end.
# 
print(new_tuple)  # Output: (1, 2, 10, 4, 5)     