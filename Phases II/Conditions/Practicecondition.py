#Practice Question for IF,ELIF,ELSE: Condition 
# Age input lo:
"""
# Below 13 → Child
# 13–19 → Teenager
# 20+ → Adult
age = int(input("Enter the age : "))
if age >= 21:
    print ("Adult")
elif age >=  13: 
    print ("Teenager")  
else:
    print("Child")  

# Second Task :
age = int(input("Enter the age : "))

if age >= 60:
    print("Senior Citizen")
elif age >= 20:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")   




# task 3 pratice question condition if, elif or else:

marks = int(input("Enter your marks: "))

percentage = marks

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("Marks:", marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)

#  Q .4 Positive ,Negative or Zero 
number = int(input("Enter the number :"))
if number > 0:
    print("Number is Positive.")
elif number < 0:
    print ("Number is Negative.")
else:
    print ("Number is Zero.")  

# Question 5 Temperature 
temperature = int(input("Enter the Temperature:"))
if temperature  >=32:
    print("Temperature is Hot")
elif temperature >= 20:
    print ("Temperature is Normal.")
else:
    print("Cold")        
"""                


# Largest of two Numbers
# a= int(input("Enter first number:"))
# b= int (input("Enter Second number:"))
# c= int(input("Enter the Third number:"))

# if a>b & a>c:
#    print ("Largest number is :" ,a  )
# elif b>c & b>a:
#    print("Largest number is :" , b) 
# elif c>a & c>b:
#    print ("Largest number is :", c)   
# else:
#    print("no largest number find out ")     


# Question : 6
# Simple Calculator:

a = int(input("Enter the First number:"))
b = int (input("Enter the second number:"))
c = input("Enter operator : ")

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
else:
    print(a / b)
