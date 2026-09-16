#Default and Keyword Arguments
#13.Default greeting
def greet (name = "vismitha"):
    return f"{name} Welcome to python"
print(greet())

#14.Calculate simple interest using a default rate
def interest (principal,time,rate=5) :
    simple_interest = (principal * rate * time) / 100
    return simple_interest
print(interest(10000,2))

#15.Student details functional using keyword
def student (name ,age , branch ,college ):
    print( f"Name:{name}\nAge:{age}\nBranch:{branch}\nCollege:{college} " )
student("vismitha",21,branch="ECE",college="ABC College")

#16.Employee details using keyword argument
def employee(name,age,salary,department):
    for key,value in locals().items():
         print (f"{key}:{value}")
employee("Rahul",25,salary=30000,department="IT")

#17.Power function where exponent has a default value of 2
def power (a,b = 2):
    return a ** b
print(power(3))
