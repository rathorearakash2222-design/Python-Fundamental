# #----------------------------------
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

#======================================================
#Question : v)Increasing triangle
# for i in range (1,6):
#     for j in range(i):
#         print("*", end =" ")
#     print()    

# Question: vi)Decreasing triangle

# for i in range (5 ,0 ,-1):
#     for j in range(i):
#         print("*", end =" ")
#     print() 

# Question : vii)Number of rows user se input lo
# n = int(input("Enter the Star's : "))
# for i in range (n):
#     for j in range(i):
#       print("*", end =" " )
#     print("*")  

# Question : viii) Right -aligned triangle

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
            