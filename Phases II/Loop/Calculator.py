# for i in range(3):
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         print("Result:", a + b)
#     elif choice == 2:
#         print("Result:", a - b)
#     elif choice == 3:
#         print("Result:", a * b)
#     elif choice == 4:
#         print("Result:", a / b)
#     else:
#         print("Invalid choice")


while True:

    print("\n----- Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    choice = int(input("Enter choice: "))
    
    if choice == 5:
            print("Calculator closed")
            break
    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        print("Result:", a / b)

    else:
        print("Invalid choice")
