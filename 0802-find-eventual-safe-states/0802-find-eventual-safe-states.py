class Solution:
    def hasCycle(self,graph,color,result,node):
        if color[node] == 1:
            return True
        if graph[node]:
            color[node] = 1
        for neighbor in graph[node]:
            if color[neighbor]!=2:
                if self.hasCycle(graph,color,result,neighbor):
                    return True
        color[node] = 2
        result.append(node)
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        result = []
        for i in range(n):
            if color[i] != 0:
                continue
            if not self.hasCycle(graph,color,result,i):
                result.append(i)
        answer = sorted(set(result))
        return answer

        