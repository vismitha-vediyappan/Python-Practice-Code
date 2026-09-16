#45.celsius to fahrenheit
a = int(input("enter the celsius:"))
formula = (a * 9/5) + 32
print(f"Fahrenheit = {formula:.2f}")

#46.fahrenheit to celsius
b = float(input("enter the fahrenheit:"))
d = (b - 32) * 5 / 9
print(f"celsius = {d:.1f}")

#47.kilometers to meters
meter = int(input("enter kilometer:"))
result = meter * 1000
print(f"meter{result:.2f}")

#48.student information program
name = input("enter name:")
age = int(input('enter age:'))
mark_1 = int(input("enter mark 1:"))
mark_2 = int(input("enter mark 2:"))
mark_3 = int(input("enter mark 3:"))
total = mark_1 + mark_2 + mark_3
average = total / 3
print("---student information---")
print("name:",name)
print("age:",age)
print(f"mark_1:{mark_1}\nmark_2:{mark_2}\nmark_3:{mark_3}")
print("total:",total)
print("average:",average)
