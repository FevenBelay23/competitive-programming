# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        queue = [(target, 0)]
        visited = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, temp in queue]
            node, temp = queue.pop(0)
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, temp+1))
        return []