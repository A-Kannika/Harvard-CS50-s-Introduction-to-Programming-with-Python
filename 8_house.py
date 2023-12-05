# Day 2: Dec 4, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 02:38:00

# use if-else
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")
elif name == "Draco":
        print("Slytherin")
else:
        print("Who?")

# Use match-case
name = input("What's your name? ")

match name:
        case "Harry" | "Hermione" | "Ron":
                print("Gryffindor")
        case "Draco":
                print("Slytherin")
        case _:
                print("Who?")