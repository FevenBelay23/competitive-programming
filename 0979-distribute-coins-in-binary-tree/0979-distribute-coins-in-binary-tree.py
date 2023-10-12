# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(curr):
            nonlocal moves
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            coin  = left + curr.val + right - 1
            moves += abs(left) + abs(right)
            return coin
        dfs(root)
        return moves
        
            
        