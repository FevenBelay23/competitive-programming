class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        len_of_queue = len(rooms)
        visited = set()
        visited.add(0)
        while queue:
            current = queue.popleft()
            for i in rooms[current]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return len(visited) == len_of_queue
        