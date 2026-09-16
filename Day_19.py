#Lambda function
#23.square a number
square = lambda x : x * x
print(square(5))

#24.Add two numbers
add = lambda x,y :x + y
print(add(10,20))

#25.Largest of two numbers
largest = lambda x,y : x if  x > y else y
print(largest(25,40))

#26.Map() to square numbers
a = [1,2,3,4,5]
square= map(lambda x : x* x ,a)
print(list(square))

#27.Filter()to exact even numbers
n = [1,2,3,4,5,6]
even = filter(lambda x :  x % 2 == 0  ,n)
print(list(even))
