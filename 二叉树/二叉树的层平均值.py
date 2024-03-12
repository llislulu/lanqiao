import collections
from typing import Optional, List

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        average = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            sum = 0
            for _ in range(size):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            average.append(sum/size)
        return average