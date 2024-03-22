from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, cur, tar):
        self.sum += cur.val
        if not cur.right and not cur.left:
            if self.sum == tar:
                return True
        if cur.left:
            if self.traversal(cur.left, tar):
                return True
            self.sum -= cur.left.val
        if cur.right:
            if self.traversal(cur.right, tar):
                return True
            self.sum -= cur.right.val
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.sum = 0

        return self.traversal(root, targetSum)


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
solution = Solution()
print(solution.hasPathSum(root, 8))
