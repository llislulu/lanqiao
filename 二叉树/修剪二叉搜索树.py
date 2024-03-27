from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if low > root.val:
            right = self.trimBST(root.right, low, high)
            return right
        if high < root.val:
            left = self.trimBST(root.left, low, high)
            return left
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


# 构造一个二叉树
#     4
#    / \
#   2   7
#  / \
# 1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
solution = Solution()
print(solution.trimBST(root, 3, 6))
