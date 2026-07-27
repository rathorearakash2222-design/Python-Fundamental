# if, elif, else condition use :

marks = int(input("Enter the marks:"))
percentage = marks 
if percentage >= 90:
    grade ="A+"
elif percentage  >= 75:
    grade ="A"
elif percentage >= 60:
    grade ="B"
else:
    grade ="C"            

print("Marks:", marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)
    