from typing import Optional, List

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def traversal(self, cur, count):
        if count == 0 and not cur.left and not cur.right:
            return self.result.append(self.path[:])
        if not cur.left and not cur.right:
            return
        if cur.left:
            count -= cur.left.val
            self.path.append(cur.left.val)
            self.traversal(cur.left, count)
            self.path.pop()
            count += cur.left.val
        if cur.right:
            count -= cur.right.val
            self.path.append(cur.right.val)
            self.traversal(cur.right, count)
            self.path.pop()
            count += cur.right.val
        return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.path.clear()
        self.result.clear()
        if not root:
            return []
        self.path.append(root.val)
        self.traversal(root, targetSum-root.val)
        return self.result


# 构造一个二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(3)
solution = Solution()
print(solution.pathSum(root, 7))