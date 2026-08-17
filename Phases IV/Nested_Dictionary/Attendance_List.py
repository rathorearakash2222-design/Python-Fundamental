students = {}

while True:

    print("\n===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Present")
    print("3. Mark Absent")
    print("4. Display Attendance")
    print("5. Attendance Percentage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ").strip()

        if not name:
           print("Student name cannot be empty!")

        elif name in students:
             print("Student already exists!")

        else:
             students[name] = "Absent"
             print("Student added successfully!")

    elif choice == "2":

       name = input("Enter student name: ").strip()

       if name in students:
        students[name] = "Present"
        print("Attendance marked Present!")
       else:
        print("Student not found!")

    elif choice == "3":

     name = input("Enter student name: ").strip()

     if name in students:
        students[name] = "Absent"
        print("Attendance marked Absent!")
     else:
        print("Student not found!")

    elif choice == "4":

      if not students:
        print("No students available!")
      else:
         print("\n===== ATTENDANCE LIST =====")

         for name, status in students.items():
            print(name, ":", status)

    elif choice == "5":

       if not students:
        print("No students available!")
       else:
               total_students = len(students)
               present_count = 0

               for status in students.values():
                 if status == "Present":
                   present_count += 1

               percentage = (present_count / total_students) * 100

               print("\n===== ATTENDANCE PERCENTAGE =====")
               print("Total Students:", total_students)
               print("Present Students:", present_count)
               print("Attendance Percentage:", percentage, "%")

    elif choice == "6":
        print("Thank you for using Attendance Management System!")
        break

    else:
        print("Invalid choice!")