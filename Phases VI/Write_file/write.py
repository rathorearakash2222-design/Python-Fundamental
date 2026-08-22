with open(r"Phases VI\Write_file\students.txt", "w") as file:
    file.write("Akash Rathore\n")
    file.write("Java Developer\n")
    file.write("Learning File Handling\n")

with open(r"Phases VI\Write_file\students.txt", "a") as file:
    file.write("Akash Rathore\n")


# with open(r"Phases VI\Write_file\students.txt", "a") as file:
#     file.write("Name: Akash\n")
#     file.write("Course: MCA\n")
#     file.write("Skill: Python\n")

# print("File written successfully!") 

with open("students.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Course: MCA\n")
    file.write("Skill: Python\n")

print("File written successfully!")   