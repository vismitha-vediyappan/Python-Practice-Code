#sys argv program(input understanding)
import sys
x = sys.argv [1]
y = sys.argv [2]
print(x,y)

#understading of dynamic padding
text = "Data"
char = "_"
width = 8 #total 8 width
padded = f"{text:{char}>{width}}"
print(padded)

#28.read and print users name
v =input("enter the name:")
print(f"the value is {v:*>15}")

#29.add two nummber
a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
c = a + b
print(f"the answer is {c:.2f}")

#30.area of rectangle
length = int(input("enter the length:"))
breadth = int(input("enter the breadth:"))
rectangle = length * breadth
print(f"area of rectangle is {rectangle:#>5}")

#31.area of circle
r = int(input("enter the radius:"))
circle = 3.14 * r**2
print(f"{circle:.1f}")

#32.simple interset
principal =int(input("enter the principal value:"))
rate = int(input("enter the rate value:"))
time = int(input("enter the time value:"))
simple_interset = (principal * rate * time) / 100
print(f"the value of interst {simple_interset:*^10}")

#33.average of three numbers
a = float(input("enter the 1st no:"))
b = float(input("enter the 2nd no:"))
c = int (input("enter the 3rd no:"))
average_number = (a + b + c) / 3
print(f"the average number is{average_number:.2f}")

#34.total bill
item_1 = int(input("enter 1st item:"))
item_2 = int(input("enter 2nd item:"))
item_3 = int(input("enter 3rd item:"))
total = item_1 + item_2 + item_3
print(f"Total = {total}")

#35.student percentage
subject_1 = int (input("enter 1st subject:"))
subject_2 = int (input("enter 2nd subject:"))
subject_3 = int (input("enter 3rd subject:"))
subject_4 = int (input("enter 4th subject:"))
subject_5 = int (input("enter 5th subject:"))
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500) * 100
print(f"percentage = {percentage:.2f}")

#36.convert minutes into to seconds
given = int(input("enter the value:"))
second = given * 60
print(second)

#37.salary calculation
input_1 = int(input("enter base salary:"))
input_2 = int(input("enter percentage:"))
bonus = input_1 * input_2 / 100
result = input_1 + bonus
print(f"Final salary = {result:.3f}")

#38.shopping discount
original_price = int(input("enter the price:"))
percentage = int(input("enter percentage:"))
discount_percentage = original_price * percentage /100
result = original_price - discount_percentage
print(f"Final price = {result:.1f}")
