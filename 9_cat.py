# Day 3: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 02:47:30 - 03:23:00

# Loops

def main() :
        x = valid_input()
        meow(x)
        print()
        meow2(x)
        print()
        meow3(x)

def valid_input() :
        while True:
                x = int(input("How many times do you want to print \"meow\"? "))
                if x > 0:
                        break
                else:
                        print ("Please provide the positive integer.")
        return x

def meow(x) :
        while (x > 0):
                print("meow")
                x -= 1

def meow2(x) :
        # We use _ because we don't need to use this variable
        for _ in range(x):
                print("meow")

def meow3(x) :
        print("meow\n" * x, end="")

main()