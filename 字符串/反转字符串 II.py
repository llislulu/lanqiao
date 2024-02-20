class Solution:
    def reverse_1(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s

    def reverseStr(self, s: str, k: int) -> str:
        rec = list(s)
        for i in range(0, len(s), 2*k):
            rec[i:i+k] = self.reverse_1(rec[i:i+k])
        return ''.join(rec)

