#13.check positive/negative/zero
num = -7
if num > 0 :
    print("positive")
elif num <  0 :
    print("negative")
else:
    print("zero")

#14.largest three numbers using nested if(differnt number)
a = 70
b = 6
c = 8
if a!= b and b != c and c != a :
    if a > b and a > c :
        print("a is greater")
    elif b > a and b > c :
        print("b is greater")
    else:
        print("c is greater")
else:
    print("invalid input")

#15.largest three numbers using nested if(same  number)
a = 70
b = 8
c = 8
if a > b:
    if a > c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b > c:
        print("b is greater")
    else:
        print("c is greater")

#16.leap year
x = 1929
if x % 400 == 0 :
    print("leap year")
elif x % 100 == 0:
    print(" not  a leap year")
elif x % 4 == 0 :
    print("leap year")
else:
    print("not a leap year")

#17.driving license based on age
age = int(input ("enter the age: "))
if age >= 18 :
    print("eligible for license")
else:
    print("not eligible")

#18.simple calculator
a = int(input("enter the number:"))
b = int(input("enter the number:"))
operator = input("enter the operator")
match operator :
   case "+" :
      print(a + b)
   case "-":
      print(a - b)
   case "*":
      print(a * b)
   case "/":
      print(a / b)
   case _ :
      print("invalid operator")



#19.display the day name using match case
day = int(input("enter the day no:"))
match day :
    case 1 :
        print("monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednesday")
    case 4 :
        print("thursday")
    case 5 :
        print("friday")
    case 6 :
        print("saturday")
    case 7 :
        print("sunday")
    case _ :
        print("invalid day")

#20.create the menu based program using match case
a = int(input("enter your choice:"))
match a :
            case 1:
              print("add")
            case 2:
                print("sub")
            case 3:
               print("multiply")
            case _:
                print("exit")
