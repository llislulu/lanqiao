class Solution:
    def reverseWords(self, s: str, n: int) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        if n > 0:
            l, r = 0, n-1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        l, r = n, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

b = int(input())
a = input()
solution = Solution()
print(solution.reverseWords(a, b))
