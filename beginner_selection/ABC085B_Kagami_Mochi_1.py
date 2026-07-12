n = int(input())

mochis = sorted([int(input()) for _ in range(n)], reverse=True)

tower = 0
prev = 0
for mochi in mochis:
    if mochi != prev:
        tower+=1
        prev = mochi
print(tower) 
