from typing import List
import profile


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backing(self, n, k, startIndex):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, n - (k - len(self.path))+1):
            self.path.append(i)
            self.backing(n, k, i + 1)
            self.path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backing(n, k, 1)
        return self.result


solution = Solution()
profile.run('solution.combine(4, 2)')
