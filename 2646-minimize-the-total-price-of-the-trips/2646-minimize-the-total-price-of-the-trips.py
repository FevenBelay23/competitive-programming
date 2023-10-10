class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph=defaultdict(list)
        answer=0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count=[0]*n
        def dfs(node,end,value,path):
            nonlocal answer
            visited[node]=1
            if node==end: 
                answer+=value+price[node]
                path+=[node]
                for i in path: count[i]+=1
                return
            for j in graph[node]:
                if visited[j]: 
                    continue
                dfs(j,end,value+price[node],path+[node])
            return value
        for k,l in trips:
            visited=[0]*n
            dfs(k,l,0,[])
        none=[0]*n
        for i in range(n):
            none[i]=(count[i]*price[i])//2
        dp1,dp2=[0]*n,[0]*n
        def dfs(node,par):
            value1,value2=0,0
            for j in graph[node]:
                if(j == par): continue
                dfs(j, node);
                value1 += dp2[j]
                value2 += max(dp1[j], dp2[j])
            dp1[node] = none[node] + value1
            dp2[node] = value2
        dfs(0,-1)
        i=max(dp1[0],dp2[0])
        min_price = answer - i
        return min_price

        