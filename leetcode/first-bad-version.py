bad = 3


def isBadVersion(n):
    return n == bad


def firstBadVersion(n: int) -> int:
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if not isBadVersion(mid) and isBadVersion(mid + 1):
            return mid + 1
        if not isBadVersion(mid):
            low = mid + 1
        else:
            high = mid - 1


print(firstBadVersion(6))
