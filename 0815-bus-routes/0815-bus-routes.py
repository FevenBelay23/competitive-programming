class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops = defaultdict(list)
        for i, j in enumerate(routes):
            for stop in j:
                stops[stop].append(i)
        visited = set()
        queue = deque([(source, 0)]) 
        while queue:
            current, num = queue.popleft()
            for bus in stops[current]:
                if bus in visited:
                    continue
                visited.add(bus)
                for stop in routes[bus]:
                    if stop == target:
                        return num + 1
                    queue.append((stop, num + 1))
        return -1
