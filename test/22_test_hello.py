# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 06:45:00 - 

# The packages, so the way to run the the test files in the folder
# To run all test file in this package, we have to create __init__.py inside the folder
# To make python treat the folder as a package

from hello_21_test_hello import hello

def main():
        test_hello()


# we cannot test the function this way 
# IF the function doesn't return anything, 
# so we cannot test the output
def test_hello():
      assert hello("Kannika") == "Hello, Kannika"

def test_default():
      assert hello() == "Hello, world"

def test_list():
       for name in ["cat", "bird", "squarrel"]:
              assert hello(name) == f"Hello, {name}"

if __name__ == "__main__":
        main()