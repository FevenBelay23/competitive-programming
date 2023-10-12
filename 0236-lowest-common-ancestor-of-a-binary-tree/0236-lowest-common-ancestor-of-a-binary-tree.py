# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr , p , q):
            if not curr:
                return None
            if curr == p or curr == q:
                return curr
            left = dfs(curr.left , p , q)
            right = dfs(curr.right , p ,q)
            if left and right:
                return curr
            return left or right
        return dfs(root , p ,q)
            
