# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.PathSum = float('-inf')
        def maximum(node):
            if not node:
                return 0
            left = max(maximum(node.left), 0)
            right = max(maximum(node.right), 0)
            current = node.val + left + right
            self.PathSum = max(self.PathSum, current)
            return node.val + max(left, right)
        maximum(root)
        return self.PathSum
        