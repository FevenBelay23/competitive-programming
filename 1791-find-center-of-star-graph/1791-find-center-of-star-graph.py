class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = {}
        for i in edges:
            for center in i:
                count[center] = count.get(center,0) + 1
                if count[center] == len(edges):
                    return center