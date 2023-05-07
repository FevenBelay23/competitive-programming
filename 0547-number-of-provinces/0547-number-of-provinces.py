class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0 
        def dfs(node):
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1 and i not in visited:
                    dfs(i)
        for node in range(n):
            if node not in visited:
                dfs(node)
                provinces += 1
        return provinces
    