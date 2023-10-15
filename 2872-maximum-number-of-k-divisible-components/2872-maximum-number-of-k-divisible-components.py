class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(curr, parent):
            nonlocal result
            total = values[curr]
            for i in graph[curr]:
                if i != parent:
                    total += dfs(i, curr)
            if total % k == 0:
                result += 1
                return 0
            return total
        
        result = 0
        dfs(0, -1)
        return result