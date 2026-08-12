
students = {
    "Akash": 56,
    "Rahul": 82,
    "Aman": 87,
    "Rohit": 91
}

while True:

    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Student Add")
    print("2. Student Search")
    print("3. Marks Update")
    print("4. Student Delete")
    print("5. All Students Display")
    print("6. Highest Marks")
    print("7. Lowest Marks ")
    print("8. Average Marks")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      name = input("Enter student name: ")

      if not name:
        print("Student name cannot be empty!")

      else:
        marks = int(input("Enter student marks: "))

        if marks < 0 or marks > 100:
          print("Marks must be between 0 and 100!")

        elif name in students:
           print("Student already exists!")

        else:
         students[name] = marks
         print("Student added successfully!")

    elif choice == "2":

        name = input("Enter student name: ")

        if name in students:
            marks = students[name]
            print("Marks:", marks)

            if marks >= 90:
              print("Grade: A+")
            elif marks >= 80:
              print("Grade: A")
            elif marks >= 70:
              print("Grade: B")
            elif marks >= 60:
              print("Grade: C")
            elif marks >= 50:
              print("Grade: D")
            else:
              print("Grade: F")

            if marks >= 40:
              print("Status: Pass")
            else:
              print("Status: Fail")
        else:
            print("Student not found!")

    elif choice == "3":

        name = input("Enter student name: ")

        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "4":

        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":

       if not students:
        print("No students available!")
       else:
        print("\n===== ALL STUDENTS =====")

        for name, marks in students.items():

            print("\nName:", name)
            print("Marks:", marks)

            if marks >= 90:
                print("Grade: A+")
            elif marks >= 80:
                print("Grade: A")
            elif marks >= 70:
                print("Grade: B")
            elif marks >= 60:
                print("Grade: C")
            elif marks >= 50:
                print("Grade: D")
            else:
                print("Grade: F")

            if marks >= 40:
                print("Status: Pass")
            else:
                print("Status: Fail")
    elif choice == "6":

        if not students:
            print("No students available!")
        else:
            highest_student = max(students, key=students.get)

            print("\n===== HIGHEST MARKS =====")
            print("Student:", highest_student)
            print("Marks:", students[highest_student])  

    elif choice == "7":

       if not students:
        print("No students available!")
       else:
        lowest_student = min(students, key=students.get)

        print("\n===== LOWEST MARKS =====")
        print("Student:", lowest_student)
        print("Marks:", students[lowest_student])

    elif choice == "8":

        if not students:
            print("No students available!")
        else:
            total = sum(students.values())
            average = total / len(students)

            print("\n===== AVERAGE MARKS =====")
            print("Average Marks:", average)

    elif choice == "9":

        print("Thank you for using Student Marks Management System!")
        break

    else:
        print("Invalid choice! Please enter 1 to 8.")

