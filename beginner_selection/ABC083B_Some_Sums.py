n, a, b = map(int, input().split())
total = 0
for num in range(1, n+1):
    digit_sum = sum(int(digit) for digit in str(num))
    
    if a<=digit_sum<=b:
        total+=num
        
print(total)
