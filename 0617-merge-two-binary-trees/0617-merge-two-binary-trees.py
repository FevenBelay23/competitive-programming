# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
          return root2
        if not root2:
          return root1
        
        if root1:
            root1_val = root1.val
        else:
            return 0
        if root2:
            root2_val = root2.val
        else:
            return 0
        new_node = TreeNode(root1_val + root2_val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)
        
        return new_node
        
        
        