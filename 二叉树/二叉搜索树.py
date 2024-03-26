from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root or val == root.val:
        #     return root
        # result = TreeNode()
        #
        # if root.val > val:
        #     result = self.searchBST(root.left, val)
        # if root.val < val:
        #     result = self.searchBST(root.right, val)
        # return result
        #迭代
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        return None
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
print(solution.searchBST(root, 2))