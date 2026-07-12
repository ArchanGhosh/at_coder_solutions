n = int(input())

cards = list(map(int, input().split()))
cards.sort(reverse=True)
score_diff = 0
switch = 1
for i in range(n):
    score_diff+=(cards[i]*switch)
    switch*=-1

print(score_diff)
