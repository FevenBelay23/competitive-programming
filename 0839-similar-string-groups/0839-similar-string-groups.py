class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        for_x = self.find(x)
        for_y = self.find(y)
        if for_x != for_y:
            self.parent[for_x] = for_y


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        
        def similar(x,y):
            different = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    different += 1
                if different > 2:
                    return False
            return different <= 2
        for i in range(n):
            for j in range(i + 1 , n):
                if i != j and similar(strs[i] , strs[j]):
                    uf.union(i,j)
        
        groups = set()
        for i in range(n):
            groups.add(uf.find(i))
        return len(groups)
                