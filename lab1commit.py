"""""
# 1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#2
b = int(input())
h = int(input())
S = 0.5 * b * h
print(S)

#3
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#4
n = int(input())
n = n % (24*60)
h = n // 60
m = n % 60
print(h,m)

#5
name = input()  
print('Hello, ' + name + '!')

#6
n = int(input())
x = n - 1
y = n + 1
print('The next number for the number ' + str(n) + ' is ' + str(y) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(x) + '.')

#7
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

#8
a = int(input()) 
b = int(input()) 
l = int(input()) 
N = int(input()) 
x = (((N*2)-1)*a) + (((N-1)*b)*2) + (2*l)
print(x)
"""