# Day 3: Dec 13, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 03:23:00 - 03:52:00

def main():
        # List
        students = ["Hermione", "Harry", "Ron", "Draco"]

        # Dictionary
        students_houses = {
                "Hermione" : "Gryffindor", 
                "Harry": "Gryffindor", 
                "Ron": "Gryffindor", 
                "Draco": "Slytherin"
        }

        # List of Dictionary
        students_house_patronus = [
                {"name" : "Hermione", "house" : "Gryffindor", "patronus": "Otter"},
                {"name" : "Harry", "house" : "Gryffindor", "patronus": "Stag"},
                {"name" : "Ron", "house" : "Gryffindor", "patronus": "Jack Russell Terrir"},
                {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
        ]
        
        print_students(students)
        print()
        print_students_with_number(students)
        print()
        print_student_with_house(students_houses)
        print()
        print_list_of_dict(students_house_patronus)

def print_students(students):
        for student in students:
                print(student)

def print_students_with_number(students):
        for i in range(len(students)):
                print(i + 1, students[i])

def print_student_with_house(students_houses):
        # use the key as an index
        for student in students_houses:
                print(student, students_houses[student], sep=", ")

def print_list_of_dict(students_house_patronus):
        # print out all students names
        for student in students_house_patronus:
                print(student["name"])
        
        print()
                
        # print out all students names with the houses
        for student in students_house_patronus:
                print(student["name"], student["house"], sep=", ")
        
        print()
                
        # print out all students names with the houses and the patronus
        for student in students_house_patronus:
                print(student["name"], student["house"], student["patronus"], sep=", ")
main()