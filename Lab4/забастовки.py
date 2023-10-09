N, K = [int(i) for i in input().split()]
strikes = [[int(i) for i in input().split()] for i in range(K)]

day_strike = set()

for i in range(K):
    for j in range(strikes[i][0], N+1, strikes[i][1]):
        if j % 7 != 0 and j % 7 != 6:
            day_strike.add(j)
print(len(day_strike))
