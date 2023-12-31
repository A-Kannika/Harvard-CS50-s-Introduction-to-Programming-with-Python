# Day 6: Dec 19, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 08:33:00 - 09:46:40

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
        # ? -> 0 or 1 repeatitions
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

        # re.IGNORECASE
        # re.MULTILINE
        # re.DOTALL

        # (\w+\.)? -> this pattern either can be or cannot be there

        # The more complex email regex from https://uibakery.io/regex-library/email-regex-python
        # r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
    
        if re.search(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email, re.IGNORECASE):
                print("Valid")
        else:
                print("Invalid")

        # the class version
        # if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
        #         print("Valid")
        # else:
        #         print("Invalid")
        
if __name__ == "__main__":
        main()