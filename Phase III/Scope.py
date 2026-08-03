def show():
    x = 10
    print(x)

show()

#Global scope
x = 10
def show():
    x = 10

show()

print(x)   


#Local vs Global
x = 100       # Global

def test():
    x = 50    # Local
    print(x)

test()
print(x)


#Global → Bahar bana variable → Mostly poore program mein accessible

#Local → Function ke andar bana variable → Sirf us function mein accessible



x = 10

def change():
    global x
    x = 20

change()

print(x)