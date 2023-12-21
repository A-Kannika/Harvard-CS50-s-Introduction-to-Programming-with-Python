# Day 7: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 09:46:40 - 10:05:00

import re

def main():
        valid_name()

def valid_name():
        name = input("What's your name? ").strip()

        # := -> if and only if
        if matches := re.search(r"^(.+), *(.+)$", name):

                name = matches.group(2) + " " + matches.group(1)

        print(f"Hello, {name}")

        # split firstname and lastname from the input
        # if "," in name:
        #         last, first = name.split(", ")
        #         name = f"{first} {last}"
        # print(f"Hello, {name}")

def valid_name1():
        name = input("What's your name? ").strip()

        matches = re.search(r"^(.+), *(.+)$", name)
        if matches:
                # method 1:
                # last, first = matches.groups()
                # name = f"{first} {last}"
                
                # method 2:
                # last = matches.groups(1)
                # first = matches.groups(2)
                # name = f"{first} {last}"

                # method 3:
                name = matches.group(2) + " " + matches.group(1)

        print(f"Hello, {name}")

        # split firstname and lastname from the input
        # if "," in name:
        #         last, first = name.split(", ")
        #         name = f"{first} {last}"
        # print(f"Hello, {name}")
        

if __name__ == "__main__":
        main()