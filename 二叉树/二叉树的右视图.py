import collections
from typing import Optional, List

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            queue_size = len(queue)
            for _ in range(queue_size):
                cur = queue.popleft()
                if _ == queue_size-1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result