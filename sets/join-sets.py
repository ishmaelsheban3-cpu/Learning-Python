# Joining Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = set1.union(set2)
print(joined_set)  # Output: {1, 2, 3, 4, 5}    

# all sets methods can be used to join sets, for example:
# Using the update() method to join sets
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}  

# using the | operator to join sets
set3 = {6, 7, 8}
set4 = {8, 9, 10}
joined_set2 = set3 | set4
print(joined_set2)  # Output: {6, 7, 8, 9, 10}  

# Using the intersection() method to find common elements between sets
set5 = {1, 2, 3, 4}
set6 = {3, 4, 5, 6}
common_elements = set5.intersection(set6)
print(common_elements)  # Output: {3, 4}    


# using the & operator to find common elements between sets
set7 = {7, 8, 9}    
set8 = {8, 9, 10}
common_elements2 = set7 & set8
print(common_elements2)  # Output: {8, 9}

# Using the difference() method to find elements in one set that are not in another
set9 = {1, 2, 3, 4}
set10 = {3, 4, 5, 6}
difference_set = set9.difference(set10)
print(difference_set)  # Output: {1, 2}


# using the - operator to find elements in one set that are not in another
set11 = {7, 8, 9}
set12 = {8, 9, 10}
difference_set2 = set11 - set12
print(difference_set2)  # Output: {7}       


# using the symmetric_difference() method to find elements that are in either set but not in both
set13 = {1, 2, 3, 4}
set14 = {3, 4, 5, 6}
symmetric_difference_set = set13.symmetric_difference(set14)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}
