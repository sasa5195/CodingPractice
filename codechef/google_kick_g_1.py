def solve():
    m, n, p = map(int, input().split())
    d = []
    mx_d = [0]*n
    ans = 0
    for i in range(m):
        row = list(map(int, input().split()))
        d.append(row)
        for j in range(n):
            mx_d[j] = max(mx_d[j], row[j])
    
    for i in range(n):
        ans +=  max(0,  mx_d[i] - d[p-1][i])
    return ans

for i in range(int(input())):
    print(f"Case #{i+1} {solve()}")
        