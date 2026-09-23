#STRING[Week 4]
a = "vismitha"
b = "bts"
char = "t"

print(a) #1.Print a String

print(len(a)) #2.Find length of a string

print(a[0]) #3.Access the first character

print(a[-1]) #4.Access the last character

#5.Print character using positive indexing
for char in range(0,8):
    print(a[char])

#6.Print character using negative indexing
for i in range (-1,-9,-1):
    print(a[i])

print(a [2:5]) #7.Print a string using slicing

print(a [::-1]) #8.Reverse a string using slicing

print (a + " " + b ) #9.Concatenate two strings

print("m" in a)#10.Check whether a character exists