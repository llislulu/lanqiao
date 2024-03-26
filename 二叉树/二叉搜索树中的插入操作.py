from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
        # cur = root
        # while cur:
        #     if val > cur.val and cur.right:
        #         cur = cur.right
        #     if val < cur.val and cur.left:
        #         cur = cur.left
        #     if val > cur.val and not cur.right:
        #         cur.right = TreeNode(val)
        #         return root
        #     if val < cur.val and not cur.left:
        #         cur.left = TreeNode(val)
        #         return root
        # return root


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
print(solution.insertIntoBST(root, 5))