class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ''
        stack = [s[0]]
        for i in range(1, len(s)):

            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)

solution = Solution()
print(solution.removeDuplicates('abbaca'))