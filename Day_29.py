#List Comprehension
#56.Create a list of squares using list comprehension
numbers = [1,2,3,4,5]
square = [n ** 2 for n in numbers ]
print(square)

#57.Create a list of even numbers using list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 == 1]#58.Create a list of odd numbers using list comprehension
print(even)
print(odd)

#59.Create a list of numbers greater than 10
numbers = [5,12,8,20,3,15,10,25]
greater = [n  for n in numbers if n > 10 ]
print(greater)

#60.Convert a list of strings into uppercase using list comprehension
words = ["python","java","sql","django"]
upper_case = [w.upper() for w in words]
print(upper_case)