#Label:- 1
#Q.1) 1 se 10 tak numbers print karo.
for i in range(0,11):
   print(i)
#---------------------------------------------------------------
#Q.2)    10 se 1 tak numbers print karo.
for i in range (10,0,-1):
   print(i) 
#---------------------------------------------------------------
#Q.3)    1 se 20 tak even numbers print karo.

for i in range (1,20):
    if i % 2==0:
        print(i)
#-----------------------------------------------------------------
# Q .4 )  1 se 20 tak odd numbers print karo. 
for i in range(1,20):
    if i % 2 !=0:
        print(i) 
#------------------------------------------------------------------
# Q.5 )1 se 50 tak numbers print karo.
for i in range (1,50):
    print(i) 
#----------------------------------------------------------------
#Q .6)  5 ka multiplication table print karo
for i in range (1,11):
      print (i * 5)  
#-----------------------------------------------------------------
#Q .7)User se number lo aur uska table print karo.       
number = int(input("Enter the Table Number :"))
for i in range (1,11):
    print(i * number)
#-----------------------------------------------------------------
# Q .8)1 se 10 tak numbers ka sum nikalo. sum = 0
for i in range (1,11):
    sum = sum + i
    print (sum)
#-----------------------------------------------------------------
#  Q .9)1 se 100 tak numbers ka sum nikalo.  
total = 0
for i in range(1,101):
    total = total + i
print(total)