#Variable Length Arguments
#18.Add any number of numbers using *args
def add (a,*b ):
    c= a + sum(b)
    return c
print(add(10,20,30,40))

#19.Find largest number using *args
def largest(a,*b):
    maximum = a
    for i in b :
        if i > maximum:
            maximum = i
    return maximum
print(largest(10,50,20,80,30))

#20.Calculate average using *args
def average(*a):
    return sum (a) / len (a)
print(average(10,20,30,40))

#21.Display student information using **kwargs
def student(**kwargs):
    for key,value in kwargs.items() :
        print(f"{key}:{value}")
student(name = "vismitha",age = 21 ,branch = "ECE")

#22.Display employee information using **kwargs
def employee (**kwargs):
    return kwargs
    print (f"{key}:{value}")
print(employee(name = "rahul",id = 101 , salary = 30000))
