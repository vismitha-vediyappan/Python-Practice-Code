#1.positive number
a = 9
if a>0 :
    print("positive number")

#2.negative or positive
b = -19
if b > 0 :
    print("postive number")
else:
    print("negative number")

#3.even or odd
v = 9
if v % 2 == 0 :
    print("even")
else:
    print("odd")

#4.larger of two number
a = 9
b = 15
if a > b :
    print("a is greater")
else:
    print("b is greater")

#5.largest three number
x = 70
y = 90
z = 100
if x > y and x > z :
    print("x is greater")
elif y > x and y > z:
    print("y is greater")
else:
    print("z is greater")

#6.voting eligibility
age =18
if age >= 18:
    print("voting eligible")
else:
    print("not eligible for voting")

#7.student pass or fail
student_mark = 87
if student_mark >= 50 :
    print("pass")
else:
    print("fail")

#8.grade calculator
student_mark = 20
if student_mark > 90 :
    print("grade A")
elif student_mark >= 50:
    print("grade B")
elif student_mark >= 35:
    print("grade C")
else:
    print("student fail")

#9.positive/negative/zero
num = 0
if num > 0:
    print("postive")
elif num < 0:
    print("negative ")
else:
    print("zero")

#10.age category
age = 9
if age >= 60:
    print("old person")
elif age >=20:
    print("youngters")
elif age >= 13:
    print("teenage people")
else:
    print("child")

#11.electricity bill
a = int(input ("enter the unit:"))
if a >= 100:
    bill = a * 5
elif a >= 200:

    bill = a * 10
elif a >= 500:
    bill = a * 25
else:
    bill = a * 50
print("electricity bill:",bill)

#12.login validation
user_name = "vismitha"
password = 12345
name = input("enter your name:")
pass_word = int(input ("enter the password:"))
if user_name == name and password == pass_word:
    print("login successfully")
else:
    print("invalid username or password")
