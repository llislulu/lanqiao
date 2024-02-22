# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # 滑动窗口法
#         left = 0
#         right = len(needle) - 1
#         while right <= len(haystack) - 1:
#             if haystack[left:right+1] == needle:
#                 return left
#             left += 1
#             right += 1
#         return -1

class Solution:
    def getnext(self, next, s) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j >= 1 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        #         KMP算法
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getnext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j >= 1 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return - 1


solution = Solution()
print(solution.strStr("adbutsad", "sad"))
