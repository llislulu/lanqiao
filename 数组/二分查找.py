def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = input()
nums = eval(nums)
target = int(input())
print(binary_search(nums, target))
