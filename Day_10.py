#FORLOOP
#21.print number from 1 to 10for i in range (1,11):
for i in range (1,11,1):
    print(i)

#22.print number from 10 to 1
for x in range (10,0,-1):
    print(x)

#23.print even number from 1 to 50
for y in range(2,51,2):
    print(y)

#24.print odd number from 1 to 50
for z in range(1,50,2):
    print(z)

#multiplication table
a = 2
for x in range(21):
    y = a * x
    print(a, "*", x, "=", y)

#25.sum from 1 to n
n= int(input("enter the number:"))
total = 0
for i in range(1,n+1):
    total = total + i
print(total)

#26.factorial of a number
a = int(input("enter the number:"))
total = 1
for i in range (a, 1, -1):
    total = total * i
print(total)

#27.count the number of digits in a number
a = (input("enter number:"))
count = 0
for i in a :
    count = count + 1
print(count)
