#keyword list
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

#docstring
import sys
print(sys.__doc__)
help(sys)

#39.convert string to integer
a = "100"
b = int(a)
print(a,"\n",type(b))

#40.convert integer to string
c = 100
d = str(c)
print(c,"\n",type(d))

#41.convert integer to float
e = 25
f = float (e)
print(e,"\n",type(f))

#42.convert float to integer
g = 15.8
h = int(g)
print(h,"\n",type(h))

#43.python keyword
import keyword
print("the keyword:")
print(keyword.kwlist)

#44.add meaning comments
#input value a,b
a = 3
b = 7
#add the inputs
c = a + b
#display output
print(c)
