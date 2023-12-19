# Day 5: Dec 18, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 08:14:00 - 08:25:00

# write to the csv file

import csv

def main():
        name = input("What's your name? ")
        home = input("What's your home? ")
        # write_file(name, home)
        write_file_dict(home, name)

# write to the csv file to the dictionary
# in the file should have the header in there
# the DictWriter will manage the right data to the right header
def write_file_dict(home, name):
        with open("students_file_dict.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "home"])
                writer.writerow({"name" : name, "home": home})

# write to the csv file
def write_file(name, home):
        with open("students_file.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([name, home])

if __name__ == "__main__":
        main()