from typing import List



# py使用集合，简洁啊
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for i in nums1:
            table[i] = table.get(i, 0) + 1
        res = set()
        for i in nums2:
            if i in table:
                res.add(i)
                del table[i]
        return list(res)

solution = Solution()
print(solution.intersection([1,2,3,3,4],[2,4,4,5,6]))