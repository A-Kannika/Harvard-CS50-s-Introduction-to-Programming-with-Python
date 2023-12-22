# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From continue from 32_student.py - go to 34_student_class_methods.py

# make the class to create the proper Student Object
class Student:
        # use ... to indent the class
        ...

def main():
        student = get_student()
        if student.name == "Padma":
                student.house = "Revenclaw"
        print(f"{student.name} from {student.house} from get_student")

def get_student():
        # careate the ojects from the Student class
        student = Student()

        # to access to the variable in the class we use the . notation
        student.name = input("Name: ")
        student.house = input("House: ")
        return student

if __name__ == "__main__":
        main()
