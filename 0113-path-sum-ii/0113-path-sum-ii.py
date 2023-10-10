# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        
        def dfs(node,target_path,target):
            if not node:
                return 
            target += node.val
            if not node.right and not node.left:
                if target == targetSum:
                    target_path.append(node.val)
                    answer.append(target_path[:])
                    target_path.pop()
                return
            target_path.append(node.val)
            dfs(node.left,target_path,target)
            dfs(node.right,target_path,target)
            target_path.pop()
                       
        dfs(root,[],0)
        return answer