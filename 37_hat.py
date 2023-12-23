# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 12:30:00 - 12:49:00

import random

# see how to use it in function hat()
class Hat:
        # placeholder
        # ...

        def __init__(self):
                self.house = ["Gryffindor", "Huflepuff", "Ravenclaw", "Slyntherin"]

        def sort(self, name):
                print(name, "is in", random.choice(self.house))

# use the @classmethod
# see how to use it in function hat2()
class Hat2:
        house = ["Gryffindor", "Huflepuff", "Ravenclaw", "Slyntherin"]

        @classmethod
        def sort(cls, name):
                print(name, "is in", random.choice(cls.house))

def main():
        hat()
        hat2()

# class Hat
def hat():
        hat = Hat()
        hat.sort("Harry")

# use class Hat2
def hat2():
        Hat2.sort("Harry")

if __name__ == "__main__":
        main()