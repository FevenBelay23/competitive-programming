class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        step = [0 for _ in range(numCourses)]
        queue = deque()
        order = []
        for course, pre in prerequisites:
            graph[pre].append(course)
            step[course] += 1
        for course in range(numCourses):
            if step[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                step[neighbor] -= 1
                if step[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != numCourses:
            return []
        return order