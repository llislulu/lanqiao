from typing import List, Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        # First
        rootvalue = preorder[0]
        root = TreeNode(rootvalue)
        if len(preorder) == 1:
            return root
        # Second
        separator_index = inorder.index(rootvalue)
        # Third
        inorder_left = inorder[:separator_index]
        inorder_right = inorder[separator_index+1:]
        # Fourth
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[len(inorder_left)+1:]
        # Fifth
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        #Sixth
        return root

