class UnionFind:
    def __init__(self, size):
        self.rep = [i for i in range(size)]
        
    def representative(self, x):
        while x != self.rep[x]:
            x = self.rep[x]
        return x
		
    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        self.rep[yrep] = xrep

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        validPath = UnionFind(n)
        for i in edges:
            validPath.union(i[0],i[1])
        answer = validPath.connected(source,destination)
        return answer