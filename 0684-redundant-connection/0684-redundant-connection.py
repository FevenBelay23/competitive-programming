class UnionFind:
    def __init__(self, size):
        self.rep={i:i for i in range(1,size+1)}
        
    def representative(self, x):
        while x != self.rep[x]:
            x = self.rep[x]
        return x
		
    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        if xrep == yrep:
            return [x,y]
        self.rep[yrep] = xrep

    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        result = 0
        Redundant = UnionFind(len(edges))
        for i,j in edges:
            result = Redundant.union(i,j)
            if result:
                return result
        return result
        