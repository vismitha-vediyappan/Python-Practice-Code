#Modulus
#37.Square root
import math
a = int (input ("enter the value:"))
print(math.sqrt(a))

#38.Factorial
import math
a = int (input ("enter the value:"))
print(math.factorial(a))

#39.Random number
import random
print(random.randint(1,100))

#40.Your own calculator module
import calculator
print(calculator.calculator(10,5))
print(calculator.odd(10))
#create the file calculator.py (code):
'''
def calculator (a,b):
   add = a + b
   sub = a - b
   mul = a * b
   div = a / b
   return add,sub,mul,div

def odd (a) :
     if a % 2 == 0:
         print("even")
     else:
        print("odd")
     return a
'''