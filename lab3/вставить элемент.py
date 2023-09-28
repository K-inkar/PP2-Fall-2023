a = input().split()
b = input().split()
a.append(b[1])
for i in range(len(a)):
    if i >= int(b[0]):
        a[i], a[-1] = a[-1], a[i]
print(*a)