# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node):
            if node is None:
                return 0
            if node in memo:
                return memo[node]
            robbed = node.val
            if node.left:
                robbed += dp(node.left.left) + dp(node.left.right)
            if node.right:
                robbed += dp(node.right.left) + dp(node.right.right)
            not_robbed = dp(node.left) + dp(node.right)
            amount = max(robbed, not_robbed)
            memo[node] = amount
            return amount
        return dp(root)