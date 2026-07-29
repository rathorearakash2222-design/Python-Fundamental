# Q.25)Number ko reverse karo.
# Example: 1234 → 4321
# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse number is:", reverse)

#String reverse
a = input("Enter string: ")
alen = len(a)

print(a)
b = ""

for i in range(alen-1,-1,-1):
    b += a[i]

print(b)