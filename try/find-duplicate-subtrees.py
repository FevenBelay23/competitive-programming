# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def duplicate(node, visited, result):
            if not node:
                return "null"
            subtree = (str(node.val) + "," + duplicate(node.left, visited, result) + "," +
                duplicate(node.right, visited, result))
            if subtree in visited:
                if visited[subtree] == 1:
                    result.append(node)
                visited[subtree] += 1
            else:
                visited[subtree] = 1
            return subtree
        
        visited = {}
        result = []
        duplicate(root, visited , result)
        return result






