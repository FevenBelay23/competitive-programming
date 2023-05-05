# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bst(preorder, first, last):
            if first >= last:
                return None
            value = preorder[first]
            root = TreeNode(value)
            i = first + 1
            while i < last and preorder[i] < value:
                i += 1
            root.left = bst(preorder, first + 1, i)
            root.right = bst(preorder, i, last) 
            return root
        return bst(preorder, 0, len(preorder))
        