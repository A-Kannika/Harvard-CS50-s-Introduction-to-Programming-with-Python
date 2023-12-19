# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 08:13:00

# if we have more than two column
# we still can use DictReader to read only the column we wanted

import csv

def main():
        open_file_dist_reader()

# use dictionary reader if your csv file first line is the header of the table
def open_file_dist_reader():

        # create empty list
        students= []

        with open("students_home_house.csv") as file:
                reader = csv.DictReader(file)

                # if in the file have exactly only column per row 
                #if not use the technique below
                for row in reader:
                        students.append({"name" : row["name"], "home" : row["home"]})
        # sorted 
        for student in sorted(students, key=lambda student: student["name"]):
                print(f"{student['name']} is from {student['home']}")

if __name__ == "__main__":
        main()