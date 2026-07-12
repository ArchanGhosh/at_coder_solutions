A_500 = int(input())
B_100 = int(input())
C_50 = int(input())

target = int(input())
total_ways = 0

for a in range(A_500 +1):
    for b in range(B_100+1):
        remaining = target - (500*a + 100*b)
        
        if remaining < 0:
            continue
        
        if remaining % 50 == 0:
            c = remaining//50
            
            if c<=C_50:
                total_ways+=1

print(total_ways)
