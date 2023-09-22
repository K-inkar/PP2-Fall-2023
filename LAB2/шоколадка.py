n = int(input())
m = int(input())
k = int(input())

ch = n * m

if ch > k and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')