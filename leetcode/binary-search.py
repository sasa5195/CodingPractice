def search(nums, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


print(search([1, 2, 3, 4, 5, 6], 5))
print(search([1, 2, 3, 4, 5, 6], 8))
print(search([1, 2, 3, 4, 5, 6, 7], 2))
print(search([1, 2, 3, 4, 5, 6, 7], 8))
