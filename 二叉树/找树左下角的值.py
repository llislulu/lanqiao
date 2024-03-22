import collections
from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


# 迭代
# class Solution:
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         global result
#         if not root:
#             return 0
#         queue = collections.deque([root])
#         while queue:
#
#             for i in range(len(queue)):
#                 cur = queue.popleft()
#                 if i == 0:
#                     result = cur.val
#                 if cur.left:
#                     queue.append(cur.left)
#                 if cur.right:
#                     queue.append(cur.right)
#         return result
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxdepth = 0
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, cur, depth):
        if not cur.left and not cur.right:
            if depth > self.maxdepth:
                self.maxdepth = depth
                self.result = cur.val
            return
        if cur.left:
            depth += 1
            self.traversal(cur.left, depth)
            depth -= 1
        if cur.right:
            depth += 1
            self.traversal(cur.right, depth)
            depth -= 1


# 构造一个二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(0)

solution = Solution()
print(solution.findBottomLeftValue(root))
