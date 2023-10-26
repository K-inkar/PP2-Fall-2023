# 1.Create a generator that generates the squares of numbers up to some number N.
def calculate_squares():
    N = int(input())  
    for i in range(1, N + 1):
        yield i ** 2 #помогатель для Generator который всегда используется в нем

s = calculate_squares()
for square in s:
    print(square)

# 2.Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(n):
    for num in range(0, n + 1, 2): # значит что начиная с 0 до n(n+1 это и есть то что показывает что до n, через 2 выводить числа)
        yield num
        
n = int(input("n: ")) #значение n 
even_numbers = even(n)
result = ', '.join(map(str, even_numbers))
print(result)

# 3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible(n):
    for number in range(n + 1):
        if number % 12 == 0:
            yield number

n = int(input())
for num in divisible(n):
    print(num)

# 4.Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(x1, x2):
    for num in range(x1, x2 + 1):
        yield num ** 2

x1 = int(input())
x2 = int(input())
for square in squares(x1, x2):
    print(square)

# 5.Implement a generator that returns all numbers from (n) down to 0.
def result(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in result(n):
    print(num)