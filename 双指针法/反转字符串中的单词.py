class Solution:
    def removeExtraSpaces(self, s):
        slow = 0
        for i in range(1, len(s)):
            if s[i] != ' ':
                if slow != 0 and slow < len(s):
                    s[slow] = ' '
                    slow += 1
                while i < len(s) and s[i] != ' ' and slow < len(s):
                    s[slow] = s[i]
                    slow += 1
                    i += 1
        return s[:slow]

    def reverseStr(self, s, left: int, right: int):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        # s = self.removeExtraSpaces(s)
        self.reverseStr(s, 0, len(s)-1)

        start = 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] == ' ':
                self.reverseStr(s, start, i-1)
                start = i + 1
        return ''.join(s)

solution = Solution()
print(solution.reverseWords("the sky is blue"))