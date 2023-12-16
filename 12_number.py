# Day 3: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 04:07:00

def main():
        x = get_int()
        print(f"x1 is {x}")

        print()
        x = get_int2()
        print(f"x2 is {x}")

        print()
        x = get_int3()
        print(f"x3 is {x}")

def get_int() :
        # Error exception
        while True:
                try :
                        x = int(input("What is x? "))       
                except ValueError:
                        print ("Please provide an integer.")
                else: 
                        break
        return x 

def get_int2() :
        # Error exception
        while True:
                try :
                        return int(input("What is x? "))       
                except ValueError:
                        print ("Please provide an integer.")

def get_int3() :
        # Error exception
        while True:
                try :
                        return int(input("What is x? "))       
                except ValueError:
                        # use pass to go to the loop without amy prompt
                        pass
main()