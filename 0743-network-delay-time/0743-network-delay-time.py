class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i, j, w in times:
            graph[i].append((j, w))
        temp = [float('inf')] * (n + 1)
        temp[k] = 0
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > temp[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < temp[neighbor]:
                    temp[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        max_dist = max(temp[1:])
        if max_dist == float('inf'):
            return -1
        return max_dist
        