# Logical Operations in If-Else Statements
x = 10
y = 20
z = 30

if x > y and x < z:
    print("x is between y and z")
elif x > y or x < z:
    print("x is either greater than y or less than z")
else:
    print("x is not between y and z")