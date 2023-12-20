# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 08:33:00

# use re library
import re

def main():
        valid_email()

def valid_email():
        # get inout from the user
        email = input("What's your email? ").strip()
        
        # use re.search to specify the pattern in email
        # . -> any character except a newline
        # * -> 0 or more repeatitions
        # + -> 1 or more repeatitions
        # r -> raw string
        # \ -> escape character
        # ^ -> matches the start of the string
        # $ -> matches the end of the string ot just before the new line at the end of the string
        # [] -> set of characters
        # [^] -> complementing the set
        # [^@] -> any character except @ -> re.search(r"^[^@]+@[^@]+\.edu$", email)
        # [a-zA-Z0-9_ ] -> the set of the characters allowed to use, a-z & A-Z & 0-9 & _ & (whitespace)
        # \w -> word character ... as well as numbers and the underscore
        # \W -> not a word character
        # \d -> decimal digit
        # \D -> not a decimal digit
        # \s -> whitespace characters
        # A|B -> either A or B -> for example (\w|\s) means word character or whitespace
        # (...) -> a group
        # (?:...) -> non-capturing version
    
        if re.search(r"^\w+@\w+\.edu$", email):
                print("Valid")
        else:
                print("Invalid")
        
if __name__ == "__main__":
        main()