def check(count, a):
    for num in a:
        if num % 2 != 0:
            return count

    a = [num // 2 for num in a]
    return check(count + 1, a)

n = int(input())
a = list(map(int, input().split()))
count = 0
print(check(count, a))
