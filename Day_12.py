#Break,Continue,Pass
#35.prime number 1 to 20 (stop at 10)
for i in range (1,21) :
    if i == 10 :
        break
    print(i)

#36.first number divisible by 7
for i in range (1,101) :
    if i % 7 == 0 :
        break
print(i)

#37.print number from 1 to 20 (skip 10)
for i in range (1,21) :
    if i == 10 :
        continue
    print(i)

#38.only odd number (continue)
for i in range(1,21):
    if i % 2 == 0 :
        continue
    print(i)

#39.search a number (using break)
x = 13
for i in range (1,51) :
      if  i == x:
           print(i)
           break
print("number found")

#40.pass inside an if
i = int(input("enter the number:"))
if  i > 0 :
    print("positive")
elif i == 0 :
    pass
else :
     print("negative")

#41.pass inside a loop
for i in range (1,21) :
    if i % 5 == 0 :
        pass
    print(i)
