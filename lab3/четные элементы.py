a=input()
x=[int(a) for a in a.split()]
for i in x:
    if int(i) % 2 == 0:
       print(i, end=' ')