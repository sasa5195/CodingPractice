def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    one_cnt, zero_cnt = 0, 0
    for i in range(k - 1, n):
        if a[i] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1

    if one_cnt == 0 or zero_cnt == 0:
        print(0)
    else:
        print(1)
    for i in range(1, k):
        print(i, i)
    print(k, n)


solve()
