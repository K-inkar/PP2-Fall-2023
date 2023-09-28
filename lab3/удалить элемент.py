s=input().split(' ')
k=int(input())
s.pop(k)
for i in range(len(s)):
    print(int(s[i]),end=' ')