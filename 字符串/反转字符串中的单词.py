class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ' '.join(s)

solution = Solution()
print(solution.reverseWords("the sky is blue"))