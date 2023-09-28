n, k = map(int, input().split())
s  = 'I' * n
s = list(s)
for i in range(k):
    l, r = map(int, input().split())
    for i in range(l - 1, r):
        s[i] = '.'
for i in s:
    print(i, end="")