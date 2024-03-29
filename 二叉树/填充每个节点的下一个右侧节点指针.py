import collections
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            prev = None
            for i in range(len(queue)):
                cur = queue.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root


# 构造一个二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
solution = Solution()
print(solution.connect(root))