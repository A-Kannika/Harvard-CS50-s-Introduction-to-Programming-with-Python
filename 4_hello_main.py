# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 01:42:00 - 01:50:41

# Organize your file: define main function at the top and call it at the bottom
# because python will execute from the top to the bottom
def main():
        name = input("What's your name? ")
        hello(name)

        x = int(input("What's x? "))
        y = int(input("What's y? "))
        z = calculator(x,y)
        print("x+y = ", z)
# hello function will print out the side effect
def hello(name = "world"):
        print("hello,", name)

# create calculate function and return the value
def calculator(x, y):
        return x + y;

main()   