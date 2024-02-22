class Solution:
    def getnext(self, next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while s[i] != s[j + 1] and j >= 0:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        # KMP
        if len(s) == 0:
            return False
        next = [0] * len(s)
        self.getnext(next, s)
        l = len(s)
        if next[l - 1] != -1 and l % (l - (next[l - 1] + 1)) == 0:
            return True
        else:
            return False
solution = Solution()
print(solution.repeatedSubstringPattern("abcabcabcabc"))