# Day 4: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From continue to 16_say.py

# sys.argv[0] -> name of the program
# sys.argv[1] -> the first argument after the name of the program
import sys

def main():
        # don't forget to comment out each function before run it 
        # because fun3 and fun4 can exit the program before fun5 and fun6 run
        fun1()
        fun2()
        fun3()
        fun4()
        fun5()
        fun6()

def fun1():# call this file with -> python3 15_name.py (Your name)
        try: 
                print("Hello, my name is", sys.argv[1])
        except IndexError:
                print("Too few arguments")

def fun2():
        if len(sys.argv) < 2:
                print("Too few arguments")
        elif len(sys.argv) > 2:
                print("Too many arguments")
        else:
                print("Hello, my name is", sys.argv[1])

def fun3():
        # exit for the IndexError
        if len(sys.argv) < 2:
                sys.exit("Too few arguments")
        elif len(sys.argv) > 2:
                sys.exit("Too many arguments")
        
        print("Hello, my name is", sys.argv[1])

def fun4():
        # exit for the IndexError
        if len(sys.argv) < 2:
                sys.exit("Too few arguments")
        
        # this will give us all arguments include the name of the program too
        for name in sys.argv:
                print("Hello, my name is", name)

def fun5():
        # exit for the IndexError
        if len(sys.argv) < 2:
                sys.exit("Too few arguments")
        
        # use slices to get only the arguments we want from the list
        # this will give us all arguments from 1 to the end
        for name in sys.argv[1:]:
                print("Hello, my name is", name)

def fun6():
        # exit for the IndexError
        if len(sys.argv) < 2:
                sys.exit("Too few arguments")
        
        # use slices to get only the arguments we want from the list
        # this will give us the arguments from 1 to 4 in the list
        for name in sys.argv[1:5]:
                print("Hello, my name is", name)

main()