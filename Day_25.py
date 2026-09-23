#LIST:BASIC AND METHODS
#21.Create and Print a List
my_list = [1, "vismitha",1.45,True]
print(my_list)

print(len(my_list))#22.Find the Length of a List

print(my_list[0])#23.Access the First element
print(my_list[-1])#23.Access the last element

#24.Print List Elements Using Indexing
for item in range(len(my_list)):
    print(my_list[item])

print(my_list[0:3])#25.Print a List Using Slicing

 #26.Update an Element in a List
my_list[1] = "python"
print(my_list)

#27.Add an Element
my_list.append("java")
print(my_list)

#28.Insert an Element at a Specific Position
my_list.insert(1,"c++")
print(my_list)

#29.Remove an Element
my_list.remove("python")
print(my_list)

#30.Remove an Element
my_list.pop()
print(my_list)