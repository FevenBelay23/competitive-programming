class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        start = [i for i in range(n+1)]
        def find(x):
            if start[x] == x:
                return x
            start[x] = find(start[x]) # path compression  
            return start[x]
        def union(x, y):
            x = find(x)
            y = find(y)
            start[x] = y
        for x, y, _ in roads:
            union(x,y)
        return min(z for x,y,z in roads if find(n) == find(x))