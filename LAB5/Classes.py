#1
class Stringg:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())

string_manipulator = Stringg()
string_manipulator.getString()
string_manipulator.printString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print(shape.area())

length = float(input())
square = Square(length)
print(square.area())

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input())
width = float(input())
rectangle = Rectangle(length, width)
print(rectangle.area())

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point1 = Point(x1, y1)
point2 = Point(x2, y2)
distance = point1.dist(point2)
print(distance)

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, poss):
        self.depos = self.balance + poss
        print(self.depos)

    def withdraw(self, negg):
        if(self.balance>=negg):
            self.withdrawal = self.balance - negg
            print(self.withdrawal)
        else:
            print('Insufficient balance')

name = input('Hello! What is your name?')
card = float(input('Enter your card details'))
account = Account(name, card)

print(f"Hello, {name}, you have {card} on your balance, press 1 if you want to deposit or Press 0 if you want to withdraw")
choice = int(input())
if(choice==1):
    add = float(input())
    account.deposit(add)
elif(choice==0):
    substract = float(input())
    account.withdraw(substract)

#6
def find_primes(numbers):
    primes = []
    for num in numbers:
        if num == 1:
            primes.append(num)
        else:
            for i in range(2, int(num/2) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers
   
    def filter_primes(self):
        return list(filter(lambda x: x in find_primes(self.numbers), self.numbers))
            
input_numbers = [int(s) for s in input().split()]
prime_filter = PrimeFilter(input_numbers)
prime_numbers = prime_filter.filter_primes()
print(prime_numbers)
