# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []
        
        while queue:
            length_of_currentlevel = len(queue)
            total_level_sum = 0
            for _ in range(length_of_currentlevel):
                current = queue.popleft()
                total_level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(total_level_sum/length_of_currentlevel)
        return result
        
    
        