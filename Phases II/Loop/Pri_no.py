# ques: 27 ) 1 se 100 tak prime numbers print karo.
# number =int(input("Enter the prime number :"))
for number in range(1, 101):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
          count = count +1
    if count == 2:

     print(number)

# n = int(input("Enter a number: "))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2: