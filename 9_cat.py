# Day 3: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 02:47:30 

# Loops

def main() :
        x = int(input("How many times do you want to print \"meow\"? "))
        meow(x)
        print()
        meow2(x)

def meow(x) :
        while (x > 0):
                print("meow")
                x -= 1

def meow2(x) :
        for i in range(x):
                print("meow")
                
main()