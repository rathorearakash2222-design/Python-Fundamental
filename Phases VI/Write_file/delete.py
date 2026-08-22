import os

os.remove("student.txt")


import os

if os.path.exists("studen.txt"):
    os.remove("student.txt")
    print("File deleted")
else:
    print("File does not exist")