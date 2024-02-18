def minSubArrayLen(target, nums):
    # 滑动窗口
    l = len(nums)
    left = 0
    right = 0
    min_len = float('inf')
    cur_sum = 0
    while right < l:
        cur_sum += nums[right]

        while cur_sum >= target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1
        right += 1
    return min_len if min_len != float('inf') else 0


nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(7, nums))
