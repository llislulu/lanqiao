import collections
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val  # 节点的值
        self.children = children if children is not None else []  # 子节点列表


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                for i in range(len(cur.children)):
                    queue.append(cur.children[i])
            result.append(level)
        return result

