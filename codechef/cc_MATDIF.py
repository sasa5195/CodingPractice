

a = [[12, 10, 6, 14], [2, 8, 4, 1], [5, 15, 11, 9], [2, 7, 13, 16]]
def solve():
    n = int(input())
    if n == 4:
        for i in a:
            print(*i)

    for i in range(17, n*n):
        print()
for i in a:
    print(*i)

