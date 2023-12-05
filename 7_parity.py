# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 02:24:30

def main():
        x = int(input("What's x? "))
        if is_even(x):
                print("Even")
        else:
                print("Odd")

def is_even(x):
        return x % 2 == 0

main()