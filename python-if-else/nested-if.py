# Nested If-Else Statements
x = 10
y = 20
z = 30

if x > y:
    if x < z:
        print("x is between y and z")
    else:
        print("x is greater than y but not less than z")
else:
    print("x is not greater than y")