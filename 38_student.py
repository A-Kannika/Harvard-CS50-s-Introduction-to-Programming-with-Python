# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 12:49:00 - 12:59:00

class Student:
        def __init__(self, name, house):
                self.name = name
                self.house = house

        def __str__(self):
                return f"{self.name} from {self.house}"
        
        # create the class method
        # the method get inside the class instead of create the get_student function below
        # we can use the get() without instanciate it
        @classmethod
        def get(cls):
                name = input("Name: ")
                house = input("House: ")
                return cls(name, house)
        
def main():
        # student = get_student()
        student = Student.get()
        print(student)

# to use this methodm we have to instanciate the class Student
# but if we create the get method inside the class using the @classmethod
# we can use the get() without instanciate it
# def get_student():
#         name = input("Name: ")
#         house = input("House: ")
#         return Student(name, house)

if __name__ == "__main__":
        main()