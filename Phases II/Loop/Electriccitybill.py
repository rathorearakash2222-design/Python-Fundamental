# Electric city bill

while 1:

    value = int(input("Enter electricity units: "))

    if value <= 50:
        bill = value * 5

    elif value <= 200:
        bill = (100 * 5) + ((value - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((value - 200) * 10)

    print("Electricity Bill:", bill)

    choice = input("Do you want to calculate again? (y/n): ")

    if choice == "n":
        print("Program End")
        break

