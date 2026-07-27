a = 40;
b = 90;
c = 30;

# if a > b:
#     print(a)
# else:
#     print(b)

if (a > b) & (a > c):
    print("Largest number is: ",a)
else:
    if b > c:
        print("Largest number is: ",b)
    else:
        print("Largest number is : ",c)
