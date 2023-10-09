n = int(input())
v = set(range(1, n + 1))
c = input()
while c!='HELP':
    m = set(map(int, c.split()))
    if len(m & v) > len(v) // 2:
        print('YES')
        v = {i for i in v if i in m}
    else:
        print('NO')
        v = {i for i in v if i not in m}
    c = input()
print(*sorted(v))
