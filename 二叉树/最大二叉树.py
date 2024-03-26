from typing import List, Optional

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # if not nums:
        #     return None
        # max_num = max(nums)
        # max_numIndex = nums.index(max_num)
        # root = TreeNode(max_num)
        # if len(nums) == 1:
        #     return root
        # if max_numIndex > 0:
        #     new_list = nums[:max_numIndex]
        #     root.left = self.constructMaximumBinaryTree(new_list)
        # if max_numIndex < len(nums) - 1:
        #     new_list = nums[max_numIndex + 1:]
        #     root.right = self.constructMaximumBinaryTree(new_list)
        # return root
        if not nums:
            return None
        max_num = max(nums)
        max_numIndex = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_numIndex])
        root.right = self.constructMaximumBinaryTree(nums[max_numIndex+1:])
        return root


solution = Solution()
solution.constructMaximumBinaryTree([1, 2, 3, 4, 5, 6, 7])
