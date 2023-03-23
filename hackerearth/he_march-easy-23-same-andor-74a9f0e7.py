def solve():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    prev = -1

    ans = 0

    for i in range(n):
        if a[i] == prev:
            cnt += 1
        else:
            ans += ((cnt * (cnt - 1)) // 2)
            cnt = 1
        prev = a[i]

    ans += ((cnt * (cnt - 1)) // 2)
    print(ans)


for _ in range(int(input())):
    solve()
