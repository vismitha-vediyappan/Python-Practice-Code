#7.Find the square of a number
def square (a):
    b = a ** 2
    return b
v = square (2)
print(v)

#8.Find the cube of a number
def cube (n):
    return n ** 3
print(cube(3))

#9.Find the largest two numbers
def largest (a,b):
    if a > b :
        return "a is largest"
    else:
        return "b is largest"
print(largest(3,2))

#10.Find the largest three numbers
def largest (a,b,c):
    if a > b and a > c:
        return "a is largest"
    elif b > a and b > c:
        return "b is largest"
    else:
        return "c is largest"
print(largest(3, 2, 5))

#11.Area of ractangle
def area (length,breadth):
    area = length * breadth
    return area
print(area(8,9))

#12.return quotient and remainder
def divide (a,b):
    c = a // b
    d = a % b
    return c,d
print (divide (10,3))
