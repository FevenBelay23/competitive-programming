# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            answer.append(root.val)
            inorder(root.right)
            
        answer = []
        inorder(root)
        
        if len(answer) == len(set(answer)):
            return answer == sorted(answer)
        
            
        
        