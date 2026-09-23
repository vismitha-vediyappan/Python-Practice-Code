#TUPLES AND SETS
#41.Create and print a tuple
tuple_1 = (1,"vismitha,",3.21,"hi",100,1,321,1)
print(tuple_1)

#42.Access elements from a tuple
print(tuple_1[0])#first element
print(tuple_1[-1])#last element

#43.Find the length of a tuple
print(len(tuple_1))

#44.Count an element in a tuple
print(tuple_1.count(1))

#45.Find the position of an element in a tuple
print(tuple_1.index(100))

#46.Unpack a tuple into variables
student = ("vismitha",21,"ECE")
a,b,c = student
print(a)

#47.Create and print a set
set_1 = {1,2,3,4,5}
print(set_1)

#48.Add elements to a set
set_1.add(6)
set_1.update((7,8))
print(set_1)

#49.Find the union of two sets
set_1 = {1,2,3,4,5,6}
set_2 = {6,7,8,9,10}
set_3 = set_1.union(set_2)
print(set_3)

#50.Find intersection and difference
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
#symmetric difference
print(set_1.symmetric_difference(set_2))
