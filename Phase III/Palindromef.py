number = int(input("Enter a number: "))

def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")

palindrome(number)