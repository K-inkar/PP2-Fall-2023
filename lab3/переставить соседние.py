A = [int(x) for x in input().split()]
for i in range(0, len(A) - 1, 2):
    A[i], A[i + 1] = A[i + 1], A[i]
for element in A:
    print(element, end=' ')
