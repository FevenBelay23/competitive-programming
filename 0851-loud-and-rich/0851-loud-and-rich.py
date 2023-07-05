class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        ans = [-1] * n
        for x, y in richer:
            graph[y].append(x)
        def dfs(node):
            if ans[node] >= 0:
                return ans[node]
            ans[node] = node  
            for neighbor in graph[node]:
                choice = dfs(neighbor)
                if quiet[choice] < quiet[ans[node]]:
                    ans[node] = choice
            return ans[node]
        for i in range(n):
            dfs(i)
        return ans
