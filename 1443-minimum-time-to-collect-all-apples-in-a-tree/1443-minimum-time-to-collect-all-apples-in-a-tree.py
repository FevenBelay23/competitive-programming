class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(node):
            visited[node] = True
            total = 0
            for k in graph[node]:
                if not visited[k]:
                    time = dfs(k)
                    if time > 0 or hasApple[k]:
                        total += 2 + time
            return total
        return dfs(0)