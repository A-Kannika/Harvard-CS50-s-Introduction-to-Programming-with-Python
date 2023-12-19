# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 07:00:00 - 07:31:00

def main():

        # add the name into the file before read
        # open_file()
        print ("Read from the file:")
        read_line()
        print()
        print ("Read and Sorted from the file:")
        read_sorted_lines()
        print()
        print ("Read and Sorted (reverse order) from the file:")
        read_reverse_sorted_lines()

# sorted (reverse order) the name from the file without adding into the list
def read_reverse_sorted_lines():

        with open("name_23_names.txt") as file:
                for line in  sorted(file, reverse=True):
                        print(f"Hello,", line.rstrip())

# sorted the name from the file without adding into the list
def read_sorted_lines():

        with open("name_23_names.txt") as file:
                for line in  sorted(file):
                        print(f"Hello,", line.rstrip())

# sorted the name from the file
def read_sorted_lines1():

        names= []
        with open("name_23_names.txt") as file:
                for line in file:
                        names.append(line.rstrip())
        for name in sorted(names):
                print(f"Hello, {name}")

# Don't need to add all lines into the list before read it
def read_line():
        with open("name_23_names.txt", "r") as file:
                for line in file:
                        print("Hello,", line.rstrip())

# read all lines for the file
def read_line1():
        with open("name_23_names.txt", "r") as file:
                # read all of the lines in the file
                lines = file.readlines()
        
        for line in lines:
                print("Hello,", line.rstrip())

# use open
def open_file():
        name = input("What's your name? ")

        # "w" for write to the file
        # but it will recreate the new file all the time
        # so everytime you run the file, 
        # it will replace the old file rather than write more info in there
        
        # file = open("name_23_names.txt", "w")

        # "a" for append to the file
        # but it will only append everything into the file
        # so we need to add the new line after add any data to the file
        
        # file = open("name_23_names.txt", "a")

        # use with so you don't have to close the file

        with open("name_23_names.txt", "a") as file:
        
        # write to the file
                file.write(f"{name}\n")
        # close to save the file
        #file.close()


def add_name_to_list():
        # create the empty list 
        names = []
        for _ in range(3):
                name = input("What's your name? ")
                names.append(name)

        # sorted the list
        for name in sorted(names):
                print(f"hello, {name}")

if __name__ == "__main__":
        main()