class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)
        def dfs(node, target):
            if node == target:
                return True
            visited[node] = True
            for k in graph[node]:
                if not visited[k] and dfs(k, target):
                    return True
            return False
        answer = []
        for query in queries:
            first, last = query
            visited = [False] * numCourses
            if dfs(first, last):
                answer.append(True)
            else:
                answer.append(False)
        return answer