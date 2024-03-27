from typing import List

letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


class Solution:
    def __init__(self):
        self.s = []
        self.result = []

    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(''.join(self.s))
            return
        digit = int(digits[index])
        letter = letters[digit]
        for i in range(0, len(letter)):
            self.s.append(letter[i])
            self.backtracking(digits, index + 1)
            self.s.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result


solution = Solution()
print(solution.letterCombinations('23'))