# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From continue from 33_student_class.py

# make the class to create the proper Student Object
class Student:
        # define the standard function () -> __init__ methods calls dunder
        # we will be able to customize this class object more
        # it's an instance method to initialize 

        def __init__(self, name, house, patronus):
                # use raise to catch an exception
                if not name:
                        raise ValueError("Missing Name")
                if house in ["Gryffindor", "Huflepuff", "Ravenclaw", "Slyntherin"]:
                        raise ValueError("Invalid house")
                self.name = name
                self.house = house
                self.patronus = patronus

        def __str__(self):
                return f"{self.name} from {self.house}"
        
        # create our own funtion
        def charm(self):
                match self.patronus:
                        case "Stag":
                                return "🐴"
                        case "Otter":
                                return "🦦"
                        case "Jack Russell terier":
                                return "🐶"
                        case _:
                                return "🐟"
                        
def main():
        student = get_student()
        print("Expecto Patronum!")
        # print(f"{student.name} from {student.house}")
        print (student.charm())

def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronous = input("Patronous: ")

        # passing an arguments to the Student class
        # treating the Student class as a function
        # we will have more control on this 
        # retrun the Student object
        return Student(name, house, patronous)

if __name__ == "__main__":
        main()
