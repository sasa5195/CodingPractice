#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    x = int(input().strip())
    if x <= 3:
        print(0)
    else:
        n3 = (x - 1) // 3
        n5 = (x - 1) // 5
        n15 = (x - 1) // 15
        s3 = (3 * n3 * (n3 + 1)) // 2
        s5 = (5 * n5 * (n5 + 1)) // 2
        s15 = (15 * n15 * (n15 + 1)) // 2
        res = s3 + s5 - s15
        print(res)
