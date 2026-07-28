# Q. 11) 1 se 50 tak sirf even numbers ka sum nikalo
for i in range (1,51):
    if i % 2==0:
     print(i)   

   #  ----------------------------------------------------------
   # 
   #  
# Q. 12) 1 se 50 tak sirf odd numbers ka sum nikalo
for i in range (1,50):
   if i %2!=0:
      print(i)

      #---------------------------------------------


#Q .13)User se n input lo aur 1 se n tak numbers print karo.
number = int(input("Enter the number :"))
for i in range(1,number + 1):
   print(i)

#------------------------------------------------

#Q .14)User se n input lo aur 1 se n tak even numbers print karo.
n = int(input("Enter the Even Number :"))
for i in range(1,n+1):
   if i % 2==0:
      print(i)

      #--------------------------------------------

      
#Q. 15)User se n input lo aur 1 se n tak odd numbers print karo.
n = int(input("Enter the Odd Number :"))
for i in range(1,n+1):
   if i % 2!=0:
      print(i)
