from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    # def __init__(self):
    #     self.pre = None
    #
    # def traversal(self, node, result):
    #     if not node:
    #         return
    #     self.traversal(node.left, result)
    #     if self.pre:
    #         result[0] = min(result[0], node.val - self.pre.val)
    #     self.pre = node
    #     self.traversal(node.right, result)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # result = []
        # result = self.traversal(root, result)
        # print(result)
        # left = 0
        # min = float('inf')
        # for right in range(1, len(result)):
        #     if result[right] - result[left] < min:
        #         min = result[right] - result[left]
        #     left += 1
        # return min
        # result = [float('inf')]
        # self.traversal(root, result)
        # return result[0]
        #迭代
        stack = []
        cur = root
        result = float('inf')
        pre = None
        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    result = min(result, cur.val-pre.val)
                pre = cur
                cur = cur.right
        return result


# 构造一个二叉树
#     5
#    / \
#   4   8
#      / \
#     7   9
root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(12)
root.right.left = TreeNode(9)
root.right.right = TreeNode(16)
solution = Solution()
print(solution.getMinimumDifference(root))
