# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 07:31:00 - 08:00:00

# csv file

def main(): 
        open_csv_file_sorted_lambda()

# sorted by students name using lambda function
def open_csv_file_sorted_lambda():

        # create the empty list to add the dictionaries 
        students = []

        with open("students.csv") as file:
                for line in file:
                        # assign the each value into different variable
                        name, house=line.rstrip().split(",")
                        # create the dictionary 
                        student = {"name" : name, "house" : house}
                        students.append(student)

        # the sorted function can call the get_name function
        for student in sorted(students, key=lambda student: student["name"]):
                print(f"{student['name']} is in {student['house']}")

# sorted by students house
def open_csv_file_sorted_house():

        # create the empty list to add the dictionaries 
        students = []

        with open("students.csv") as file:
                for line in file:
                        # assign the each value into different variable
                        name, house=line.rstrip().split(",")
                        # create the dictionary 
                        student = {"name" : name, "house" : house}
                        students.append(student)

        # create this function to help with sorted by name of students
        def get_house(student):
                return student["house"]
        # the sorted function can call the get_name function
        for student in sorted(students, key=get_house):
                print(f"{student['name']} is in {student['house']}")


# reverse sorted by students name
def open_csv_file_sorted_reverse():

        # create the empty list to add the dictionaries 
        students = []

        with open("students.csv") as file:
                for line in file:
                        # assign the each value into different variable
                        name, house=line.rstrip().split(",")
                        # create the dictionary 
                        student = {"name" : name, "house" : house}
                        students.append(student)

        # create this function to help with sorted by name of students
        def get_name(student):
                return student["name"]

        # the sorted function can call the get_name function
        for student in sorted(students, key=get_name, reverse=True):
                print(f"{student['name']} is in {student['house']}")


# sorted by students name
def open_csv_file_sorted():

        # create the empty list to add the dictionaries 
        students = []

        with open("students.csv") as file:
                for line in file:
                        # assign the each value into different variable
                        name, house=line.rstrip().split(",")
                        # create the dictionary 
                        student = {"name" : name, "house" : house}
                        students.append(student)

        # create this function to help with sorted by name of students
        def get_name(student):
                return student["name"]

        # the sorted function can call the get_name function
        for student in sorted(students, key=get_name):
                print(f"{student['name']} is in {student['house']}")

# create the csv file
def open_csv_file():
        with open("students.csv") as file:
                for line in file:
                        # assign the each value into different variable
                        name, house=line.rstrip().split(",")
                        print(f"{name} is in {house}")

# open the csv file
def open_csv_file1():
        with open("students.csv") as file:
                for line in file:

                        # assign the values from each line into the row (list)
                        # then access each varible using index
                        row=line.rstrip().split(",")
                        print(f"{row[0]} is in {row[1]}")

if __name__ == "__main__":
        main()