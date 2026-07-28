number = int(input("Enter the number :"))
if number  > 0 or number < 0:
    print("number are not zero")
else:
    print("number are zero.")  
#-------------------------------------------------------------------
# check the number are divisible of 5 
number = int(input("Enter the number :"))   
if number % 5==0:
    print("Enter number is divisible by 5.")
else:
    print("Number are not divisible by 5")    

#------------------------------------------------------------------
#Electricity units input lo aur bill category print karo:
number = int(input("Enter the Number : "))
if number <=100:
   print ("Low")
elif number <=300:
    print ("Medium")
else:
    print("High")       