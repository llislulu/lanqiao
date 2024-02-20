from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = set()
        for i, num in enumerate(nums):
            cur_sum = target - num
            if cur_sum in table:
                return [nums.index(cur_sum), i]
            table.add(num)
        return []


solution = Solution()
print(solution.twoSum([1, 2, 3, 9, 9, 3], 6))
