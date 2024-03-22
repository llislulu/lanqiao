import collections
from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # queue = collections.deque([root])
        # maxDp = 0
        # while queue:
        #     maxDp += 1
        #     for i in range(len(queue)):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        # return maxDp
        # 递归前序遍历
        return self.deep(root)
    def deep(self, node) -> int:
        if not node:
            return 0
        leftnode = self.deep(node.left)
        rightnode = self.deep(node.right)
        maxDp = 1 + max(leftnode, rightnode)
        return maxDp

# 构造一个二叉树
#      1
#     / \
#    2   3
#   / \
#  4   5
# /
# 7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
solution = Solution()
print(solution.maxDepth(root))
