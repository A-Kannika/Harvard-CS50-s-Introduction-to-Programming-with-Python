# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From continue from 34_student_class_methods.py - 12:24:30

# make the class to create the proper Student Object
class Student:
        # define the standard function () -> __init__ methods calls dunder
        # we will be able to customize this class object more
        # it's an instance method to initialize 

        def __init__(self, name, house):
                self.name = name
                self.house = house

        def __str__(self):
                return f"{self.name} from {self.house}"
        
        # properties
        # use @property to make python theat this method as a getter
        @property
        def name(self):
                return self._name
        
        # decorators
        # make this methods to the setter
        # this setter method will get call anytime we use .house
        # for example student.house
        @name.setter
        def name(self, name):
                # use raise to catch an exception
                if not name:
                        raise ValueError("Missing Name")
                self._name = name

                # properties
        # use @property to make python theat this method as a getter
        @property
        def house(self):
                return self._house
        
        # decorators
        # make this methods to the setter
        # this setter method will get call anytime we use .house
        # for example student.house
        @house.setter
        def house(self, house):
                if house not in ["Gryffindor", "Huflepuff", "Ravenclaw", "Slyntherin"]:
                        raise ValueError("Invalid house")
                self._house = house
                            
def main():
        student = get_student()
        # print(f"{student.name} from {student.house}")
        print(student)
      

def get_student():
        name = input("Name: ")
        house = input("House: ")

        # passing an arguments to the Student class
        # treating the Student class as a function
        # we will have more control on this 
        # retrun the Student object
        return Student(name, house)

if __name__ == "__main__":
        main()
