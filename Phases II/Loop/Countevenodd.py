# q.21) 1 se 100 tak numbers mein kitne even numbers hain, count karo.
count = 0

for i in range(1, 101):
    if i % 2 == 0:
        count = count + 1

print("Total even numbers:", count)

#Q.22)1 se 100 tak numbers mein kitne odd numbers hain, count karo.
count = 0

for i in range(1, 101):
    if i % 2 != 0:
        count = count + 1

print("Total odd numbers:", count)