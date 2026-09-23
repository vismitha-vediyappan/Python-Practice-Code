#LIST:PROBLEM SOLVING
#31.Find the Sum of All Numbers in a List
numbers = [10,10,20,30,40,50,50]
print(sum(numbers))

print(max(numbers))#32.Find the Largest Element

print(min(numbers))#33.Find the Smallest Element

#34.Count Occurrences of an Element
count = numbers.count(10)
print(count)

#35.Find the Position of an Element
position = numbers.index(30)
print(position)

#36.Sort a List in Ascending Order
numbers.sort()
print(numbers)

#37.Sort a List in Descending Order
numbers.sort(reverse = True)
print(numbers)

#38.Reverse a List
number = [10,20,30,40,50]
number.reverse()
print(number)

#39.Find Even Numbers from a List
a = [10,15,22,31,40,53]
for i in a :
    if i % 2 == 0:
        print(i)

#40.Find Odd Numbers from a List
numbers = [10,15,22,31,40,53]
for i in numbers:
    if i % 2 != 0:
        print(i)