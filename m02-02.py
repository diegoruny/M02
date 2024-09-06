"""
Author: Diego Delgado Torres
File: m02-02.py
Description: This script prompts the user to input student names and their GPAs.
             It then determines if the student qualifies for the Dean's List or the Honor List
             based on their GPA. The process continues until the user inputs 'ZZZ' as the student name.
"""


def qualify_for():
    name = str(input('Student Name: '))
    while name != 'ZZZ':
        gpa = float(input('Student GPA: '))
        if gpa >= 3.5:
            print(f"The student {name} qualifies for the Dean's List with a GPA of {gpa}")
            continue
        elif gpa < 3.5:
            print(f"The student {name} qualifies for the Honor List with a GPA of {gpa}")
            continue
        else:
            print("This student is not elegible for any of the list")
            continue
    return


print(qualify_for())
