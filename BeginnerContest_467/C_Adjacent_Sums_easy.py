n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = float('inf')

for first in [0, 1]:
    x = [0] * n
    x[0] = first

    for i in range(n - 1):
        x[i + 1] = x[i] ^ B[i]

    cost = 0
    for i in range(n):
        if x[i] != (A[i] % 2):
            cost += 1

    answer = min(answer, cost)

print(answer)
