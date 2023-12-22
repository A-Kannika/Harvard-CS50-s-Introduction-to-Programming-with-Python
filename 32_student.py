# Day 8: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 10:37:30

def main():
        name = get_name()
        house= get_house()
        print(f"{name} from {house} from get_name() and get_house()")

        print()
        name, house = get_student_touple()
        print(f"{name} from {house} from get_student_touple")

        print()
        student = get_student_touple()
        print(f"{student[0]} from {student[1]} from get_student_touple using indexes")

        print()
        student = get_student_list()
        if student[0] == "Padma":
                student[1] = "Revenclaw"
        print(f"{student[0]} from {student[1]} from get_student_list")

        print()
        student = get_student_dict()
        if student["name"] == "Padma":
                student["house"] = "Revenclaw"
        # use 'name' and 'house' inside the " "
        # good way to use dict because you can use keys (no index) -> less confused
        print(f"{student['name']} from {student['house']} from get_student_dict")

        print()
        student = get_student_dict2()
        if student["name"] == "Padma":
                student["house"] = "Revenclaw"
        # use 'name' and 'house' inside the " "
        # good way to use dict because you can use keys (no index) -> less confused
        print(f"{student['name']} from {student['house']} from get_student_dict2")

# how to return multiple values
# this actually return dictionary with thier keys
def get_student_dict2():
        name = input("Name: ")
        house = input("House: ")
        return {"name" : name, "house" : house}

# how to return multiple values
# this actually return dictionary with thier keys
def get_student_dict():
        student = {}
        student["name"] = input("Name: ")
        student["house"] = input("House: ")
        return student

# how to return multiple values
# this actually return list with 2 values
# List is mutable
def get_student_list():
        name = input("Name: ")
        house = input("House: ")
        return [name, house]

# how to return multiple values
# this actually return touple with 2 values
# Touple is immutable
def get_student_touple():
        name = input("Name: ")
        house = input("House: ")
        return name, house


def get_name():
        return input("Name: ")

def get_house():
        return input("House: ")

if __name__ == "__main__":
        main()