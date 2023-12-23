# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 12:59:00

# suppose we have Student and Professor classes
# and both classed have variable name
# so we can see that there are some same (duplicate) codes 
# we can create another class to help -> Wizard class

class Wizard:
        def __init__(self, name):
                if not name:
                        raise ValueError("Missing name")
                self.name = name
        
        ...

# Student class and Professor class can inherit Wizard class
# mean Student and Professor classes are the sub-class of Wizard class
# in the other hand, the Wizard class is the super class of Student and Professor classes
# how to use access the parent class, we will use super().__init__(...)
class Student(Wizard):
        def __init__(self, name, house):
                # if not name:
                #         raise ValueError("Missing name")
                # self.name = name
                super().__init__(name)
                self.house = house
        
        ...

class Professor(Wizard):
        def __init__(self, name, subject):
                # if not name:
                #         raise ValueError("Missing name")
                # self.name = name
                super().__init__(name)
                self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
