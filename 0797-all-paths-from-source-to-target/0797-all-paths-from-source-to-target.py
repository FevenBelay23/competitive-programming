class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, curr):
            if node == len(graph) - 1:
                result.append(curr)
            else:
                for i in graph[node]:
                    dfs(i, curr + [i])
        result = []
        dfs(0, [0])
        return result