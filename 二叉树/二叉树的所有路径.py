from typing import Optional, List

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, cur, path, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            sPath = "->".join(map(str, path))
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        if not root:
            return []
        self.traversal(root, path, result)
        return result


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
solution = Solution()
print(solution.binaryTreePaths(root))