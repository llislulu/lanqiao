import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        pri_que = []
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(pri_que)[1]
        return res


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 3, 3], 3))
