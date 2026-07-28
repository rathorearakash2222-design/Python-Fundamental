# while loop → jab condition ke basis par repeat karna ho.
i = 1

while i <= 5:
    print(i)
    i = i + 1


#----------------------

#Q.24)

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits:", sum)