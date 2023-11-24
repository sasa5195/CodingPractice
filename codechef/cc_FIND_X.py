import math


def solve():
    a, b, c, d = map(int, input().split())

    if (a + 1) % b == (c + 1) % d:
        print(1)
    else:
        smallest_a = a - (a % b)
        lcm_bd = (b * d) // math.gcd(b, d)
        print(smallest_a + lcm_bd - a)

    lcm_bd = (b * d) // math.gcd(b, d)
    for i in range(1, lcm_bd + 1):
        if (a + i) % b == (c + i) % d:
            print(i)
            break


for _ in range(int(input())):
    solve()

