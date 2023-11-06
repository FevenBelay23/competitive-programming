# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def check(node, is_root):
            if not node:
                return None
            remove = node.val in to_delete
            if is_root and not remove:
                result.append(node)
            node.left = check(node.left, remove)
            node.right = check(node.right, remove)
            return None if remove else node

        result = []
        check(root, True)
        return result





