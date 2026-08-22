import csv
import os

FILE_NAME = r"D:\Akash Python Fundamental\Phases VI\Miniproject\Students.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Course", "Marks"])

create_file()

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, course, marks])

    print("Student added successfully!")

add_student()

def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            print("--------------------")

view_students()  

