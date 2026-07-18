n = int(input())

price, paid, status = [], [], []

for _ in range(n):
    pr, pd, st = input().split()
    price.append(int(pr))
    paid.append(int(pd))
    status.append(st)

lost = 0

for i in range(n):
    if status[i] == "keep":
        lost += paid[i] - price[i]

print(lost)
