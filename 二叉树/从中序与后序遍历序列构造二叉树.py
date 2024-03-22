from typing import List, Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, inorder, postorder):
        # 第一步：空节点
        if len(postorder) == 0:
            return None
        # 第二步：后序遍历数组最后一个元素，就是当前的中间节点
        rootvalue = postorder[-1]
        root = TreeNode(rootvalue)
        # 叶子节点
        if len(postorder) == 1:
            return root
        # 第三步：找切割点
        separator_index = inorder.index(rootvalue)
        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_index]
        inorder_right = inorder[separator_index + 1:]
        # 第五步：切割postorder数组. 得到postorder数组的左,右半边.
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]
        # 第六步：递归
        root.left = self.traversal(inorder_left, postorder_left)
        root.right = self.traversal(inorder_right, postorder_right)
        # 第七步：返回
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.traversal(inorder, postorder)


solution = Solution()
solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
