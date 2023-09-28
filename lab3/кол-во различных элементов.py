a = [int(i) for i in input().split()]
dis = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        dis += 1
print(dis)