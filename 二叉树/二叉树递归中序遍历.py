from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def aux(p):
            if p:
                aux(p.left)
                res.append(p.val)
                aux(p.right)
        aux(root)
        return res

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

# 创建 Solution 类的实例
solution = Solution()

# 调用前序遍历函数并输出结果
print(solution.inorderTraversal(root))