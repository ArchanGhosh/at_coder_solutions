n, m = map(int, input().split())

ops = []

for _ in range(m):
    r, c = map(int, input().split())
    ops.append((r, c))

seen_rows = set()
seen_cols = set()

ans = 0

for r, c in reversed(ops):
    if r not in seen_rows and c not in seen_cols:
        ans += 1

    seen_rows.add(r)
    seen_cols.add(c)

print(ans)
