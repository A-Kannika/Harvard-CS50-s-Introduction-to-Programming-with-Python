# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 06:09:15

from calculator_20_test_calculator import square

def main():
        test_square()

# install pytest: pip3 install pytest
# and call pytest (file name)
def test_square():
        assert square(2) == 4
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0

# instead of write all test case by yourself
# you can use the pytest
def test_square1():
        # automatically test the program
        # AssertionError
        try:
                assert square(2) == 4
        except AssertionError:
                print("2 squared was not 4")
        try:
                assert square(3) == 9
        except AssertionError:
                print("3 squared was not 9")
        try:
                assert square(-2) == 4
        except AssertionError:
                print("-2 squared was not 4")
        try:
                assert square(-3) == 9
        except AssertionError:
                print("-3 squared was not 9")
        try:
                assert square(0) == 0
        except AssertionError:
                print("0 squared was not 0")

if __name__ == "__main__":
        main()