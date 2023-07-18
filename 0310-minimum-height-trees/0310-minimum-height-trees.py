class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        root = deque()
        for node in graph:
            if len(graph[node]) == 1:
                root.append(node)
        while n > 2:
            count = len(root)
            n -= count
            for _ in range(count):
                leaf = root.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf) 
                if len(graph[neighbor]) == 1:
                    root.append(neighbor)
        return list(root)