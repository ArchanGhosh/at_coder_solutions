n, k = map(int, input().split())

A, B = [], []

for _ in range(n):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

base = sum(A)
gain = [b - a for a, b in zip(A, B)]

NEG = -10**30

end = [NEG] * (k + 1)
best = [NEG] * (k + 1)

best[0] = 0

for x in gain:
    for j in range(k, 0, -1):
        end[j] = max(end[j] + x, best[j - 1] + x)
        best[j] = max(best[j], end[j])

ans = base
for j in range(k + 1):
    ans = max(ans, base + best[j])

print(ans)
