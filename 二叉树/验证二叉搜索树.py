from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def __init__(self):
        self.pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # left = self.isValidBST(root.left)
        # if self.pre is not None and self.pre.val >= root.val:
        #     return False
        # self.pre = root
        # right = self.isValidBST(root.right)
        # return left and right
        #迭代
        stack = []
        pre = None
        cur = root
        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right




# 构造一个二叉树
#     5
#    / \
#   4   8
#      / \
#     7   9
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
solution = Solution()
print(solution.isValidBST(root))
