import collections
from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 层序遍历
        # if not root:
        #     return 0
        # queue = collections.deque([root])
        # sum = 0
        # while queue:
        #     for i in range(len(queue)):
        #         sum += 1
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        # return sum
        # 迭代前序遍历
        # if not root:
        #     return 0
        # stack = [root]
        # sum = 0
        # while stack:
        #     sum += 1
        #     cur = stack.pop()
        #     if cur.right:
        #         stack.append(cur.right)
        #     if cur.left:
        #         stack.append(cur.left)
        # return sum
        # 递归前序遍历
        if not root:
            return 0
        self.count = 0

        def p(root):
            if not root:
                return
            self.count += 1

            p(root.left)
            p(root.right)
        p(root)
        return self.count
