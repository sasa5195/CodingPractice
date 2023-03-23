import math

n, m = map(int, input().split())
a = []
row_tot = []
col_tot = []
for i in range(n):
    row = list(map(int, input().split()))
    row_tot.append(sum(row))
    a.append(row)

for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum+=a[i][j]
    col_tot.append(col_sum)


max_val = -1
max_x = math.inf
max_y = math.inf
for i in range(n):
    for j in range(m):
        rook_pow = row_tot[i] + col_tot[j] - (2*a[i][j])
        if rook_pow == max_val:
            if max_x == i:
                max_y = min(max_y, j)
            elif max_x > i:
                max_x = i
                max_y = j
        elif rook_pow > max_val:
            max_val = rook_pow
            max_x = i
            max_y = j

print(max_x+1, max_y+1)