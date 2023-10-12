# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        queue = [(root,0)]
        
        if not root:
            return 0
        
        while queue:
            level = len(queue)
            temp,start = queue[0]
            
            for i in range(level):
                curr , idx = queue.pop(0)
                if curr.left:
                    queue.append((curr.left , idx*2))
                if curr.right:
                    queue.append((curr.right, idx*2 +1))
            
            width = max(width , idx-start +1)
        return width
        