# Recursion
# 28.Print 1 to n
def num(n):
    if n == 1:
        print(n)
    else:
        num(n - 1)
        print(n)
num(5)

# 29.Print n to 1
def number(n):
    if n == 1:
        print(n)
    else:
        print(n)
        number(n - 1)
number(5)

# 30.Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# 31.Sum 1 to n
def add(n):
    if n == 1:
        return n
    else:
        return n + add(n - 1)
print(add())

# 32.Fibonacci number
def fibo(a, b, count):
    if count == 0:
        return
    print(a)
    fibo(b, a + b, count - 1)
fibo(0, 1, 6)

# 33.Sum of digits
def sum_n(n, count):
    if n == 0:
        return count
    b = n % 10
    n = n // 10
    return sum_n(n, count + b)
print(sum_n(1123, 0))
