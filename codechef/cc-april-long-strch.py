def get_all_substrings(string, length):
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield(string[i:j])


# for i in range(int(input())):
#     n = int(input())
#     s,c = input().split()
#     res = 0
#     for sub_str in get_all_substrings(s, n):
#         if c in sub_str:
#             res += 1
#     print(res)

for tst in range(int(input())):
    n = int(input())
    s,c = input().split()
    char_until_given_ltr = 0
    tot_possiblities = int((n*(n+1))/2)
    for i in s:
        if i == c:
            tot_possiblities = tot_possiblities - (int((char_until_given_ltr*(char_until_given_ltr+1))/2))
            char_until_given_ltr = 0
        else:
            char_until_given_ltr = char_until_given_ltr + 1
    if char_until_given_ltr != 0:
        tot_possiblities = tot_possiblities - (int((char_until_given_ltr * (char_until_given_ltr + 1)) / 2))
        char_until_given_ltr = 0
    print(tot_possiblities)