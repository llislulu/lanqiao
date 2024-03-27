from typing import List


class Solution:
    def backtracking(self, candidates, target, number_sum, startIndex):
        if number_sum == target:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            if number_sum + candidates[i] > target:
                continue
            number_sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, number_sum, i+1)
            number_sum -= candidates[i]
            self.path.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.result


solution = Solution()
print(solution.combinationSum([10,1,2,7,6,1,5], 8))
