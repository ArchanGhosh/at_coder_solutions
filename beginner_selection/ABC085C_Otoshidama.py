'''
This is one of the first Mathematically Heavy problems that I faced, so Adding the logic on solution.

Given N - > no.of Bills
      Value - > total valuation

My first approach was using two loops one for x and one for y and finding z by z = N - (x + y) resulting in O(n2)

But then this problem can be also dong in O(n) and it took sometime to figure this out

x + y + z = N ............. eqn 1

10000x + 5000y + 1000z = Value
10x + 5y + z = Value / 1000 .......... Eqn 2

Substract eqn 1 from eqn 2

10x + 5y + z - (x + y +z ) = (Value / 1000) - N

9x + 4y = (Value/1000) - N

We now write (Value/1000) - N as D

So,
D = 9x + 4y

or 

y = (D - 9x) / 4 

With this all we need is x as we can represent both y and z in terms of x
'''


def solve(no_of_bills, total_value):
    D = total_value // 1000 - no_of_bills

    for x in range(no_of_bills + 1):
        r = D - 9 * x
        if r < 0:
            break
        if r % 4 != 0:
            continue

        y = r // 4
        z = no_of_bills - x - y

        if z >= 0:
            print(x, y, z)
            return

    print(-1, -1, -1)
    
no_of_bills, total_value = map(int, input().split())
solve(no_of_bills, total_value)
