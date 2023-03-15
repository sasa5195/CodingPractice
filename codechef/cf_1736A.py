def solve():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  diff = 0
  az = a.count(0)
  bz = b.count(0)
  for i in range(n):
    if a[i] != b[i]:
      diff +=1
  ans = min(diff, 1 + abs(az-bz))
  print(ans)
    

for _ in range(int(input())):
  solve()