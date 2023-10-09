class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (x, y) in enumerate(edges):
            probability = succProb[i]
            graph[x].append((y, probability))
            graph[y].append((x, probability))  
        max_probability = [0.0] * n
        priority = [(-1.0, start_node)]  
        max_probability[start_node] = 1.0
        while priority:
            prob, node = heapq.heappop(priority)
            prob = -prob  
            if node == end_node:
                return prob
            for neighbor, temp in graph[node]:
                new = prob * temp
                if new > max_probability[neighbor]:
                    max_probability[neighbor] = new
                    heapq.heappush(priority, (-new, neighbor))
        return 0.0 