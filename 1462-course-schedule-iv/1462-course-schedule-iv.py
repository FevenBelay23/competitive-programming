class Solution:
    def can_reach(self,graph, start, target):
        queue = deque([start])
        visited = set()
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            if node in visited:
                continue
            visited.add(node)
            queue.extend(graph[node])
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[0]].append(i[1])
        answer = []
        for j in queries:
            start, target = j[0], j[1]
            answer.append(self.can_reach(graph, start, target))
        return answer


