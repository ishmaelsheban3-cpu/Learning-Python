# Looping Through Tuple Elements
# example
sample_tuple = (1, 2, 3, 4, 5)

# Looping through all elements
for element in sample_tuple:
    print(element)  # Output: 1, 2, 3, 4, 5

# Looping through indices
for i in range(len(sample_tuple)):
    print(f"Index {i}: {sample_tuple[i]}")  

# More examples
cars_model = ("Toyota", "Honda", "Ford")

for brand in cars_model:
    print(brand)  # Output: Toyota, Honda, Ford

for i in range(len(cars_model)):
    print(f"Index {i}: {cars_model[i]}")    