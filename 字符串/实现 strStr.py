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
    def strStr(self, haystack: str, needle: str) -> int:
#         KMP算法


solution = Solution()
print(solution.strStr( "sadbutsad", "sad"))