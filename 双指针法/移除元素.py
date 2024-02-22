from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

solution = Solution()
print(solution.removeElement([1,2,2,4], 2))