from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ('+', '-', '*', '/'):
                stack.append(int(tokens[i]))
            else:

                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(b - a)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '/':
                    stack.append(int(b / a))
        return stack[-1]


solution = Solution()
print(solution.evalRPN(["4","13","5","/","+"]))
