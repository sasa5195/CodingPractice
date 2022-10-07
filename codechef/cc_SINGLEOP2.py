def brute():
  s = "0"
  a = int(s,2)
  print(s, a)
  for i in range(1, len(s)+1):
    print(i, bin((a//(2**i)))[2:], a^(a//(2**i)))

brute()


def solve():
  n=int(input())
  s = input()
  fs = s.lstrip("0")
  ans = fs[1:].find("1")
  if ans == -1:
    print(len(fs))
  else:
    print(ans + 1)

for _ in range(int(input())):
  solve()
