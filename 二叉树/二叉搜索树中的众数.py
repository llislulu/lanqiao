from typing import Optional, List

from 二叉树.二叉树迭代前序遍历 import TreeNode


class Solution:
    def traversal(self, node: Optional[TreeNode], man) -> List[int]:
        if not node:
            return man
        if node.left:
            self.traversal(node.left, man)
        man.append(node.val)
        if node.right:
            self.traversal(node.right, man)
        return man
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        man = self.traversal(root, [])
        count = 0
        max_count = 0
        last = None
        ans = []
        for i in man:
            if i == last:
                count += 1
            else:
                count = 1
            if count > max_count:
                ans = [i]
                max_count = count
            elif count == max_count:
                ans.append(i)
            last = i
        return ans


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(12)
root.right.left = TreeNode(9)
root.right.right = TreeNode(12)
solution = Solution()
print(solution.findMode(root))
