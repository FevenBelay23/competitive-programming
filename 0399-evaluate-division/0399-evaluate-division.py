class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (nume, denume), value in zip(equations, values):
            graph[nume][denume] = value
            graph[denume][nume] = 1 / value
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for i, value in graph[start].items():
                if i not in visited:
                    result = dfs(i, end, visited)
                    if result != -1.0:
                        return result * value
            return -1.0
        answer = []
        for j in queries:
            start, end = j
            visited = set()
            result = dfs(start, end, visited)
            answer.append(result)
        return answer
        