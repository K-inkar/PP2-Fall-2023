a = int(input())
aa = int(input())
b = int(input())
bb = int(input())

if (a == b) or (aa == bb):
    print('YES')
elif abs(a - b) == abs(aa - bb):
    print('YES')
else:
    print('NO')