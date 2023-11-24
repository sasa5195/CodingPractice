import random


def solve(x):
    # x = int(input())
    a = int(x ** 0.5)
    b = a - 1
    c = x - (a*b)
    if 1 <= a <= (10 ** 6) and 1 <= b <= (10 ** 6) and 1 <= c <= (10 ** 6):
        # print("Yes", a, b, c, x)
        return
    else:
        print("No", x, a, b, c)


for _ in range(1000000):
    x = random.randint(10000000000, 10**12)
    # print(x)
    solve(x)
