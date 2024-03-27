from typing import List


class Solution:
    def backtracking(self, s, startIndex):
        if startIndex == len(s):
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(s)):
            if self.is_palindrome(s, startIndex, i):
                self.path.append(s[startIndex:i+1])
                self.backtracking(s, i + 1)
                self.path.pop()

    def is_palindrome(self, s, startIndex, end):
        i: int = startIndex
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.path = []
        self.backtracking(s, 0)
        return self.result


solution = Solution()
print(solution.partition("aab"))
