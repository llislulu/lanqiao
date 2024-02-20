from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        umap = dict()
        for i in nums1:
            for j in nums2:
                if i+j in umap:
                    umap[i+j] += 1
                else:
                    umap[i+j] = 1
        for p in nums3:
            for q in nums4:
                key = -p - q
                if key in umap:
                    count += umap[key]
        return count


solution = Solution()
print(solution.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[4, 100]))
