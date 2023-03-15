from collections import defaultdict


def solve(n, k):
    mp = defaultdict(bool)
    tot = 0
    for _ in range(k):
        a = input()
        if a[2] == "I":
            _, t = a.split()
            mp[t] = not mp[t]
            if mp[t]:
                tot += 1
            else:
                tot = max(0, tot - 1)
        else:
            tot = 0
            mp = defaultdict(bool)
        print(tot)


n, k = map(int, input().split())
solve(n, k)
