def sortedSquares(nums):
    i = 0
    j = len(nums) - 1
    k = len(nums) - 1
    result = [float('inf')] * len(nums)
    while i <= j:
        if nums[i] * nums[i] < nums[j] * nums[j]:
            result[k] = nums[j] * nums[j]
            j -= 1
        else:
            result[k] = nums[i] * nums[i]
            i += 1
        k -= 1
    return result


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
