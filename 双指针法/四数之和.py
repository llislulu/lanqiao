from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= 0 and nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] >= 0 and nums[i] + nums[k] > target:
                    break
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] + nums[i] + nums[k] > target:
                        right -= 1
                    elif nums[left] + nums[right] + nums[i] + nums[k] < target:
                        left += 1
                    else:
                        result.append([nums[left], nums[right], nums[i], nums[k]])
                        while right > left and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result
