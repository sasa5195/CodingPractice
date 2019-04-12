# Hackland is being attacked by Greyland, and you have been assigned the job to save it. Your enemies, known as Grey hats, are numbered starting from L to R, both inclusive. But, here is the fun part: Grey hats are known to switch sides, and you need to make full use of it to get some of them on your side.
#
# Now, two Grey hats are said to be dangerous if they form a volatile pair. A volatile grey hat pair is one where i<=j * K and j<=i * K, where 'i' and 'j' are the numbers of Grey hats (i != j). So, basically you can't afford a dangerous grey hat pair in your army.
#
# Now given L,R and K, find the maximum number of Grey hats you can get to your side, such that no two of them form a volatile pair.
#
#
# Input Format:
# First line contains T, the number of test cases. T lines follow.
# Each line consists of 3 space seperated number denoting L, R and K.
#
#
# Output Format:
# For each test case, print the answer, the maximum number of Grey hats you can get to your side.
#
#
# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ L ≤ R ≤ 106
# 1 ≤ K ≤ 103
#
# SAMPLE INPUT
# 2
# 1 10 10
# 1 11 10
# SAMPLE OUTPUT
# 1
# 2
# Explanation
# Test Case 1: L=1, R=10, K=10. Every pair of number between 1 to 10 with K=10 will form a volatile pair. Thus, you can have maximum of 1 grey hat on your side.
#
# Test Case 2: L=1, R=11, K=10. We can have 1 and 11, since they do not form a volatile pair. So you can have maximum of 2 grey hats on your side.
#

# for t in range(int(input())):
#     a,b,k=map(int, input().split())
#     res = 0
#     for i in range(a,b+1,k):
#         res = res + 1
#     print(res)

for t in range(int(input())):
    a,b,k=map(int, input().split())
    res = 0
    ht = []
    for i in range(a,b+1):
        for j in range(i+1, b+1):
            if not (i <= j*k and j <= i*k):
                ht.append(i)
                ht.append(j)
                print(i,j)
                res = res + 1
    print(res+1)
    print(len(set(ht)))