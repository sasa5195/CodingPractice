
def solve():
    n, k = map(int, input().split())
    a = input()
    cur_len = 0
    flg = False
    for i in range(n):
        if a[i] == "*":
            cur_len += 1
        else:
            if cur_len >= k:
                flg = True
                break
            cur_len = 0
    if flg:
        print("YES")
    else:
        if cur_len >= k:
            print("YES")
        else:
            print("NO")



for _ in range(int(input())):
    solve()
