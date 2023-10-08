class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        prereq = defaultdict(set)
        for i, j in prerequisites:
            graph[i].append(j)
            prereq[j].add(i)
        result = {}
        for course, tar in queries:
            if course not in result:
                visited = set()
                queue = deque([course])
                match = False
                while queue:
                    current = queue.popleft()
                    if current == tar:
                        match = True
                        break
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                result[(course, tar)] = match
        return [result[(course, tar)] for course, tar in queries]
        