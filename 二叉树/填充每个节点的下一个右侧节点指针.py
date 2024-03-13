from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        queue = collections.deque([root])