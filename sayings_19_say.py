# Day 4: Dec 15, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 06:00:15 - 06:09:15
# Create our own library to use with the 19_say.py

# Use main to see the results from each function
def main():
        hello("world")
        goodbye("world")

def hello(name):
        print(f"Hello, {name}")

def goodbye(name):
        print(f"Goodbye, {name}")

# give main the condition
# so the main will not get call 
# when you import this library to another program
if __name__ == "__main__":
        main()