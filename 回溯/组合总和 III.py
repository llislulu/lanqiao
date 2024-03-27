from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtracking(self, k, n, startIndex):
        if sum(self.path) > n:
            return
        if sum(self.path) == n and len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, 10 - (k - len(self.path))+1):
            self.path.append(i)
            self.backtracking(k, n, i + 1)
            self.path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.result


solution = Solution()
print(solution.combinationSum3(3, 9))
