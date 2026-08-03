number = int(input("Enter a number: "))

def armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** digits)
        num = num // 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

armstrong(number)