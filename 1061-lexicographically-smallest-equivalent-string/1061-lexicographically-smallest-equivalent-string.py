class UnionFind:

    def __init__(self):
        self.root = list(range(26))
    
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        for_x, for_y = self.find(x), self.find(y)
        if for_x == for_y:
            return
        if for_x < for_y:
            self.root[for_y] = for_x
        else:
            self.root[for_x] = for_y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            first, second = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            uf.union(first, second)
        answer = []
        for j in baseStr:
            i = ord(j) - ord('a')
            new = chr(uf.find(i) + ord('a'))
            answer.append(new)
        return ''.join(answer)
