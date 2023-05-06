class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        node = set()  
        for i in edges:
            node.add(i[1])
        answer = list(set(range(n)) - node)
        return answer