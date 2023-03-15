import random
from collections import Counter

MOD = (10 ** 9) + 7


def gen_list():
    a = []
    for i in range(1, 100):
        a += [i] * random.randint(11, 20)
    print(len(a), Counter(a))
    return a


def solve():
    n = int(input())
    a = Counter(map(int, input().split()))

    # test_list = gen_list()
    # a = Counter(test_list)

    tot = 0
    if a[1] == 0:
        print(tot)
        return
    tot = a[1]
    prev = a[1]
    i = 2
    while a[i] > 0:
        prev *= a[i]
        tot += prev
        if tot >= MOD:
            tot = tot % MOD

        i += 1
    print(tot % MOD)


for _ in range(int(input())):
    solve()
