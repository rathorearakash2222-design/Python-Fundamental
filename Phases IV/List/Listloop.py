#Day 3: List Looping & Traversing

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
#========================================================================
#while Loop se List Print Karna

fruits = ["Apple", "Banana", "Mango"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1  

#========================================================================
#Index ke Saath Print Karna
fruits = ["Apple", "Banana", "Mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


#List ka Sum
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

print("Sum =", total)



# Maximum  Number
numbers = [10, 40, 15, 90, 30]

print(max(numbers))

#Minimum Number
numbers = [10, 40, 15, 90, 30]

print(min(numbers))