import csv

file_path = "Phases VI/Write_file/students.csv"

# Read CSV
with open(file_path, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Write CSV
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Akash", 22, 85])
    writer.writerow(["Rahul", 21, 78])
    writer.writerow(["Aman", 22, 91])


# Search Student
search_name = input("Enter student name: ")

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"] == search_name:
            print(row)