class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestor = [0] * n
        adjacent = defaultdict(list)
        for u, v in edges:
            adjacent[u].append(v)
            ancestor[v] += 1
        result = [set() for _ in range(n)]
        nodes = deque([i for i in range(n) if ancestor[i] == 0])
        while nodes:
            current_node = nodes.popleft()
            for next_node in adjacent[current_node]:
                result[next_node].add(current_node)
                result[next_node] |= result[current_node]
                ancestor[next_node] -= 1
                if ancestor[next_node] == 0:
                    nodes.append(next_node)
        return list(map(sorted, result))
        