a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (c >= b):
    print(b)
elif (b >= a) and (c >= a):
    print(a)
else:
    print(c)