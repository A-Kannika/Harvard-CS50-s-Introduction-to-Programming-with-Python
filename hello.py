# Day 1: Dec 2, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From

# Look at python document at docs.python.org

# This is one line comment

""" This is 
the multiple
lines 
comments
"""

# Take input from the user then assign it to the 'name' variable
name = input("What's your name? ")
print("Hello, " + name + ".") 

lastname = input("What's your lastname? ")
# Pass more then 1 argument to the function
# Print will automatically add 1 space for you
print("Hello,", name, lastname)

# Look for the docs for print function
# docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *objects means print function can take many objects
# sep=' ' means print with passing multiple argument will automatically add one single space
# end='\n' means after one function print finish, it will be automatically fo to the next line
print()
print("Hello, ")
print(name, lastname)

# to remove the new line, add end=""
print()
print("Hello, ", end="")
print(name, lastname)

# to change the softspace
print()
print("Hello,", name, lastname, ".", sep='?????')

# print " use '"' or \"
print()
print("Hello, \"my friend\"")

# another special way passing the argument, use f
print()
print(f"Hello, {name}" )

# remove whitespace on the left and on the right from string
name = name.strip()
print()
print(f"Hello, {name}" )

# Capitalize the input, only the first character
name = name.capitalize()
print()
print(f"Hello, {name}" )

# Title, Capitalize the input, every word
name = name.title()
print()
print(f"Hello, {name}" )

# Remove whitespce and capitalize all words
name = name.capitalize().title()
print()
print(f"Hello, {name}" )

print()
# You can use multiple methods at the same time
# Take input, remove whitespace, and capitalize all words
name = input("What's your name? ").strip().capitalize().title()
print(f"Hello, {name}" )
print()

# Find your own style and team's style

# Split user's name into first name into first name and last name by whitespace
first, last = name.split(" ")
print(f"Hello, {first}" )
