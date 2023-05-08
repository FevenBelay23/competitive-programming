class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        colors = [0] * (n+1)
        def dfs(node, color):
            colors[node] = color
            for k in graph[node]:
                if colors[k] == color:
                    return False
                if colors[k] == 0 and not dfs(k, -color):
                    return False
            return True
        for node in range(1, n+1):
            if colors[node] == 0 and not dfs(node, 1):
                return False
        return True