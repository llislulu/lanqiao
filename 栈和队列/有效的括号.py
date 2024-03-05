class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(')')
            elif s[i] == "[":
                stack.append("]")
            elif s[i] == "{":
                stack.append("}")
            elif len(stack) == 0 or stack[-1] != s[i]:
                return False
            else:
                stack.pop()
        print(stack)
        return len(stack) == 0


solution = Solution()
print(solution.isValid("(11)"))
