# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 01:35:00 - 01:42:00

# create hello the function
def hello():
        print("hello")

name = input("What's your name? ")
hello()
print(name)

# pass variable into function
def hello2(name):
        print("hello,", name)

name = input("What's your name? ")
hello2(name)

# pass variable into function with the defualt value
def hello3(name = "world"):
        print("hello,", name)

hello3()
name = input("What's your name? ")
hello2(name)