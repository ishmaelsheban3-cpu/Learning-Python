# Bitwise Operators - used to perform bitwise operations on integers. 
# These operators work on the binary representation of integers and perform operations bit by bit.
# Compares numbers at the binary level and returns a new number based on the operation performed.
# Example:
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x & y)  # Output: 1 (Binary: 0001)
print(x | y)  # Output: 7 (Binary: 0111)
print(x ^ y)  # Output: 6 (Binary: 0110)
print(~x)     # Output: -6 (Binary: ...1010)
print(x << 1) # Output: 10 (Binary: 1010)
print(x >> 1) # Output: 2 (Binary: 0010)    

# I dont understand what you mean by "I dont u". Could you please clarify or provide more context?
# On how you get the ones and zeros in the binary representation of a number, you can use the built-in `bin()` function in Python. For example:
number = 5
print(bin(number))  # Output: 0b101     

# More examples with negative numbers:
negative_number = -5    
print(bin(negative_number))  # Output: -0b101       

# More examples with larger numbers:
large_number = 1024 
print(bin(large_number))  # Output: 0b10000000000