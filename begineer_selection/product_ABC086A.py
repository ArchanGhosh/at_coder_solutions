a,b = map(int,(input().split(" ")))


def check(a, b):
    if a==1:
        if b%2==0:
            return "Even"
        else:
            return "Odd"
    elif b==1:
        if a%2==0:
            return "Even"
        else:
            return "Odd"
    else:
        if a%2==0 and b%2==0:
            return "Even"
        elif a%2!=0 and b%2!=0:
            return "Odd"
        else:
            return "Even"

print(check(a, b))
    
