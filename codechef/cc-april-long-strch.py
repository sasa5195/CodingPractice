def get_all_substrings(string, length):
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield(string[i:j])


for i in range(int(input())):
    n = int(input())
    s,c = input().split()
    res = 0
    for sub_str in get_all_substrings(s, n):
        if c in sub_str:
            res += 1
    print(res)
