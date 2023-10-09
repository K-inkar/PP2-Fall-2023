list = int(input())

a = set()

for _ in range(list):
    word = input()
    words = word.split()

    a.update(words)

print(len(a))
