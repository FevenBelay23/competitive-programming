class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 
        current = 0  
        total = 0  
        n = len(gas)
        for i in range(n):
            total += gas[i] - cost[i]  
            current += gas[i] - cost[i]  
            if current < 0:
                current = 0
                start = i + 1
        if total >= 0:
            return start
        else:
            return -1
                     
        