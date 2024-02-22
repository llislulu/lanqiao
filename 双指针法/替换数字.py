class Solution:
    def t(self, s: str) -> str:
        count = 0
        t = list(s)
        for i in t:
            if '0' <= i <= '9':
                count += 1
        t = t + [''] * count * 5
        i = len(s) - 1
        j = len(t) - 1
        while i < j and j >= 0:
            if '0' <= t[i] <= '9':
                t[j] = 'r'
                t[j - 1] = 'e'
                t[j - 2] = 'b'
                t[j - 3] = 'm'
                t[j - 4] = 'u'
                t[j - 5] = 'n'
                j -= 5
            else:
                t[j] = t[i]
            i -= 1
            j -= 1
        return ''.join(t)

solution = Solution()
print(solution.t('asd22222d'))