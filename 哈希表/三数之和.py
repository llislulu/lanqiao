from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:  # i去重
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                # 去除重复数值
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                # 指针收缩
                    left += 1
                    right -= 1
        return result
