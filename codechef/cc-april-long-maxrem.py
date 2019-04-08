n = int(input())
a = set(map(int, input().split()))
if len(a) > 1:
    a = sorted(list(a))
    print(a[-2])
else:
    print(0)