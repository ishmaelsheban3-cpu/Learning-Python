# Ternary Operator
x = 5
y = 10
z = x if x > y else y
print(z)  
# Output: 10  #explanation: 
# The ternary operator is a shorthand way of writing an if-else statement. 
# In this example, if x is greater than y, z will be assigned the value of x; 
# otherwise, z will be assigned the value of y. Since x (5) is not greater than y (10), 
# z will be assigned the value of y (10).  
# 
# More examples of the ternary operator:
a = 15
b = 20
c = a if a > b else b
print(c)  # Output: 20  

# Another example:
age = 18
status = "adult" if age >= 18 else "not adult"
print(status)  # Output: adult
# explanation: In this example, if age is greater than or equal to 18, 
# status will be assigned the value "adult"; otherwise, 
# it will be assigned "not adult". Since age (18) is equal to 18, 
# status will be assigned "adult".

# another example:
num = -5
result = "negative" if num < 0 else "not negative"
print(result)  # Output: negative   

# last example:
temperature = 30