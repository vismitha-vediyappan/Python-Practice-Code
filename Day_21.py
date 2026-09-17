#Scope
#34.Demonstrate a local variable
def create ():
    a = 10
    b = 20
    return a + b
print(create())

#35.Demonstrate a global variable
a = 10
b = 20
def add ():
    return a + b
print(add())

#36.Modify a global variable using global
a = 5000
def balance ():
    global a
    a = a + 2000
    return a
print(balance())