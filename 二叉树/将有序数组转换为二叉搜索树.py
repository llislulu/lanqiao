from typing import List, Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, nums, left, right):
        if left >right:
            return None
        mid = left + (right - left)/2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums) - 1)
