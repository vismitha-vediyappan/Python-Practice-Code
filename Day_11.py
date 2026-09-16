#WHILE LOOP
#28.print number from 1 to 10
i = 0
while i <= 9 :
    i += 1
    print(i)

#29.print number from 10 to 1
i = 10
while i >= 1 :
    print(i)
    i -= 0

#30.even number from 1 to 50
i = 0 #not using %
while i <= 49 :
    i += 2
    print(i)

i = 0 #using %
while i <= 50 :
    if i % 2 == 0:
        print(i)
    i += 1

#31.sum of digits of number
i = 325
total = 0
while i  > 0 :

    digits = i % 10
    total= digits + total
    i = i // 10
print(total)

#32.reverse the number
i = 98765
total = 0
while i > 0 :
    x = i % 10
    total = total * 10 + x
    i = i // 10
print(total)

#33.count  the digits of number
x = 65784390
total = 0
while x > 0 :
     x = x // 10
     total = total + 1
print(total)

#34. factorial number
x = 4
total = 1
while x > 1 :
    total  = x * total
    x = x - 1
print(total)
