#Q.16)Kisi number ka factorial find karo.
number = int(input("Enter the number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print("Factorial is:", factorial)

