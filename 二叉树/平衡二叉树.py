from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.deep(root) != -1:
            return True
        else:
            return False

    def deep(self, node) -> int:
        if not node:
            return 0
        leftNode = self.deep(node.left)
        if leftNode == -1:
            return -1
        rightNode = self.deep(node.right)
        if rightNode == -1:
            return -1
        if abs(leftNode - rightNode) > 1:
            return -1
        else:
            return max(leftNode, rightNode) + 1


# 构造一个二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
solution = Solution()
print(solution.isBalanced(root))