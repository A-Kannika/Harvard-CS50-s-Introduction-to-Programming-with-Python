# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 01:50:41 - 02:16:00

# compare values: conditionals
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
        print("x is less than y")
elif x == y:
        print("x is equal to y")
else:
        print("x is greater than y")

# two conditionals with or operator
if x < y or x > y:
        print("x is not equal to y")
else:
        print("x is equal to y")

# Better way to compare only one condition rather than 2 or more
if x != y:
        print("x is not equal to y")
else:
        print("x is equal to y")