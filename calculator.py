# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 01:04:00 - 01:35:00


# 1 int
x = 1
y = 2
z = x + y
print(z)

# take input from user (as a string)
x = input("What's x? ")
y = input("What's y? ")
# cast to int before calculation
z = int(x) + int(y)
print(z)

# cast the intput to int before calculation
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# !!!Don't try to make your code to complex, make it in the simple way
# print(int(input("What's x? ")) + int(input("What's y? ")))

# 2 float
x = float(input("What's x? "))
y = float(input("What's y? "))
# turn ou the float answer
print(x + y)

# round the answer to the nearest integer
# in the doc: round(number[, ndigits]) -> defualt to the nearest integer
z = round(x + y)
print(z)

# output with the comma for the number that greater than 999
print(f"{z:,}")

# specific number of digits
z = round(x / y, 2)
print(z)

# or 
z = x / y
print(f"{z:.2f}")
print(f"{z:.3f}")
print(f"{z:.4f}")