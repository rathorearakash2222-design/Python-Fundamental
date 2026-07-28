# Conditions are used to make decisions in your program using 
# statements like if, elif, and else.

                 # Simple Condition 

age = 18 
if age >= 18:
  print ("You are an adult." )
#--------------------------------------------------------------
            # Using  if and else condition :

number = int(input("Enter the number :")) 
if number % 2==0:
  print ("Number is Even. ")
else:  
  print  ("Number is Odd. ") 
#--------------------------------------------------------------------
#   Exam Pass or Fail
#Rule:

# Marks 40 ya usse zyada → Pass
# Marks 40 se kam → Fail

marks = int(input("Enter the marks:"))
if marks >=50:
  print("Pass")
else:
  print("Fail")  
#-----------------------------------------------------------------
  # Multiple Condition :

 # AND

#Age 18+ AND Indian citizen → Eligible  

age = 21
citizen = True
if age >= 18 and citizen == True:
  print ("You are an Eligible . ")
else:
  print ("You are not Eligible .")  
#-------------------------------------------------------------------
   #  OR
#Agar student ke paas ID card OR Admit Card hai → Entry allowed.
id_card = False
admit_card = True
if id_card == True or admit_card == True:
  print ("Entry allowed")
else:
  print ("Not allowed")
#--------------------------------------------------------------------
  # NOT 
rain = True

if not rain:
    print("Go outside")
else:
    print("Stay at home")
