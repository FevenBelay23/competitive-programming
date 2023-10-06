class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda i: i[0] - i[1])
        total = 0
        n = len(costs) // 2  
        for i in range(n):
            total += costs[i][0] 
        for i in range(n, len(costs)):
            total += costs[i][1] 
        return total