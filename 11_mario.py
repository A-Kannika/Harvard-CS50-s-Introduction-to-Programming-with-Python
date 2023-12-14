# Day 3: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 03:52:00 - 04:07:00

def main():
        print_column(3)
        print_row(4)
        print()
        print_square(3)
        print()
        print_square2(4)
        

def print_column(height):
        for _ in range(height):
                print("#")
                
        # or print("#\n" * height, end="")

def print_row(width):
        print("#" * width)

def print_square(size):
        # for each row in square
        for i in range(size):

                # for each brick in row
                for j in range(size):

                        # print brick
                        print("#", end="")
                # print the new line
                print()

# use print row to print the brick
def print_square2(size):
        # for each row in square
        for i in range(size):
                print_row(size)

main()

