#44.Right triangle
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

#45.reverse triangle
for i in range (5,0,-1):
    for j in range (i):
        print("*",end ="")
    print()

#46.number triangle
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#47.number triangle
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

#48.square pattern
for i in range (1,6):
    for j in range (5):
        print("*",end="")
    print()

#49.Right-aligned triangle
for i in range (1,6):
    for j in range(5-i):
        print(" ",end="")

    for j in range (i):
        print("*",end ="")
    print()

#50. Continuous Number Triangle
number = 1
for i in range (1,5):
    for j in range (i):
        print(number,end="")
        number = number + 1
    print()
