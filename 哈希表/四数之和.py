from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > target > 0 and nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] > target and target > 0:
                    break
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                left = k + 1
                right = len(nums) - 1
                while left < right:
                    sum_ = nums[i] + nums[k] + nums[left] + nums[right]
                    if sum_ < target:
                        left += 1
                    elif sum_ > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[k], nums[left], nums[right]])
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        while right > left and nums[left] == nums[left + 1]:
                            left += 1
                        right -= 1
                        left += 1
        return result
