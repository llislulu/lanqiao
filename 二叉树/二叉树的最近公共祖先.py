class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left and not right:
            return left
        if not left and right:
            return right
        else:
            return None

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
print(solution.lowestCommonAncestor(root, root.right.left, root.right.right))
