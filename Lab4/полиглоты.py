n = int(input())
all = set()
personal = set()
know = set()
for i in range(n):
    summ = int(input())
    for j in range(summ):
        personal.add(input())
    if i == 0:
        know = personal
    all |= personal
    know &= personal
    personal = set()
print(len(know))
for i in sorted(know):
    print(i)
print(len(all))
for i in sorted(all):
    print(i)