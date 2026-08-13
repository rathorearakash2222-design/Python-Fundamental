# Contact Book  - Second Mini Project

contacts = {
    "Akash": "9876543210",
    "Rahul": "9876501234"
}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

      name = input("Enter contact name: ").strip()

      if not name:
        print("Contact name cannot be empty!")

      elif name in contacts:
        print("Contact already exists!")

      else:
        phone = input("Enter phone number: ").strip()

        if not phone.isdigit():
            print("Phone number must contain only digits!")

        elif len(phone) != 10:
            print("Phone number must be 10 digits!")

        else:
            contacts[name] = phone
            print("Contact added successfully!")
    elif choice == "2":
        name = input("Enter contact name: ").strip()

        if name in contacts:
           print("Phone:", contacts[name])
        else:
           print("Contact not found!")

    elif choice == "3":

        name = input("Enter contact name: ").strip()

        if name in contacts:
           new_phone = input("Enter new phone number: ")
           contacts[name] = new_phone
           print("Contact updated successfully!")
        else:
           print("Contact not found!")

    elif choice == "4":

         name = input("Enter contact name: ").strip()

         if name in contacts:
          del contacts[name]
          print("Contact deleted successfully!")
         else:
          print("Contact not found!")

    elif choice == "5":

        if not contacts:
           print("No contacts available!")
        else:
           print("\n===== ALL CONTACTS =====")

           for name, phone in contacts.items():
               print(name, ":", phone)

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")