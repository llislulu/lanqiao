class Solution:
    def test(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] in ['1','2','3','4','5','6','7','8','9']:
                s[i] = 'number'
        return ''.join(s)
a = input()
solution = Solution()
print(solution.test(a))