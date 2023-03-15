from itertools import permutations


def check(a, n):
    tot = a[0]
    flg = True
    for i in range(2, n + 1):
        tot += a[i - 1]
        if tot % i == 0:
            flg = False
            break
    return flg


# def gen_perm(n):
#     a = list(range(1, n + 1))
#     a_perm = list(permutations(a))
#     for perm in a_perm:
#         if check(perm, n):
#             print(perm)


def gen_perm(n):
    a = list(range(n, 0, -1))
    for i in range(2, n, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
    if check(a, n):
        print(a)
    else:
        print(f"{n} nahi hua{a}")


for i in range(4, 19,2):
    print(f"--------------{i}--------------")
    gen_perm(i)
