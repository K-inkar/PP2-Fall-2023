a = [int(i) for i in input().split()]
x = int(input())
rost = 0
while rost < len(a) and a[rost] >= x:
    rost += 1
print(rost + 1)
