from typing import Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def __init__(self):
        self.pre = None
    def traversal(self, node):
        if not node:
            return node
        if node.right:
            self.traversal(node.right)
        if self.pre:
            node.val = node.val + self.pre.val
        self.pre = node
        if node.left:
            self.traversal(node.left)
        return node
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.traversal(root)