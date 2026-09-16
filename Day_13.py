#EFFECTIVE PROGRAM FOR LOOP CONDITION
#37.prime number
n = int(input("enter the number:"))
for i in range(2,n) :
    if n % i == 0 :
        print(" not prime number")
        break
else:
    print(" prime number")

# using chatgpt exact correct answer
n = int(input("enter the number:"))
if n <= 1:
    print("not prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not prime number")
            break
    else:
        print("prime number")

#38.palindrome number
n = int (input("enter value:"))
original = n
reverse = 0
while n > 0 :
    digit  = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse :
    print ("palindrome")

else:
    print ("not palindrome")

#39.armstrong number
x = int (input("enter the number:"))
original = x
am_no =0
while x > 0 :
    take  = x % 10
    am_no = am_no + take ** 3
    x = x // 10
if original == am_no :
    print("armstrong number")
else:
    print("not armstrong number")

#40.fibonacci series
m = int(input("enter first no:"))
n = int(input ("enter second no:"))
N = int (input('enter value'))
for i in range(N):
    print(m)
    x = m + n
    m = n
    n = x

#41.sum of digits
a = int (input("enter the value:"))
total = 0
while a > 0 :
    b = a % 10
    total = total + b
    a = a // 10
print(total)

#42.reverse the number
a = int (input("enter the value:"))
total = 0
while a > 0 :
    b =  a % 10
    total = total * 10 + b
    a = a // 10
print(total)

#43.perfect number
a = int (input ("enter the value:"))
total = 0
for i in range (1,a):
    if  a % i == 0 :
       total =  total + i
if total == a :
    print("perfect number" )
else:
    print("not perfect number")
