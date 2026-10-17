# Operator Precedence
# In Python, operator precedence determines the order in which operators are evaluated in an expression.
# Operators with higher precedence are evaluated first.
# For example:
x = 5
y = 10
z = 2
print(x + y * z)  # Output: 25 (because multiplication has higher precedence than addition)
print((x + y) * z)  # Output: 30 (because parentheses have the highest precedence)  


# More examples of operator precedence:
# Exponentiation has higher precedence than multiplication and division
print(2 ** 3 * 4)  # Output: 32 (because exponentiation has higher precedence than multiplication)
print(2 ** (3 * 4))  # Output: 256 (because parentheses have the highest precedence)    