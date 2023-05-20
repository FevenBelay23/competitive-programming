class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        result = [0] * n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(node):
            subnode = defaultdict(int)
            subnode[labels[node]] += 1
            for k in graph[node]:
                graph[k].remove(node)
                child_subnode = dfs(k)
                for label, count in child_subnode.items():
                    subnode[label] += count
            result[node] = subnode[labels[node]]
            return subnode
        dfs(0)  
        return result





