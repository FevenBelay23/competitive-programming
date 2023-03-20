# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_PathSum = float('-inf')
        def max_sum(node):
            if not node:
                return 0
            left = max(max_sum(node.left), 0)
            right = max(max_sum(node.right), 0)
            curr_sum = node.val + left + right
            self.max_PathSum = max(self.max_PathSum, curr_sum)
            return node.val + max(left, right)
        
        max_sum(root)
        return self.max_PathSum
        