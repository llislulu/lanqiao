from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, cur, result):
        if not cur:
            return
        if not cur.left and not cur.right:
            return

        if cur.left:
            self.traversal(cur.left, result)
        if cur.left and not cur.left.left and not cur.left.right:
            result.append(cur.left.val)
        if cur.right:
            self.traversal(cur.right, result)


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = []
        if not root:
            return 0
        self.traversal(root, result)
        sum = 0
        for i in result:
            sum += i
        return sum

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
root.right.left = TreeNode(3)
solution = Solution()
print(solution.sumOfLeftLeaves(root))