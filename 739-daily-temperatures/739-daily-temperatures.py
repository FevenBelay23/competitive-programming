class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer, ms = len(temperatures), [0]
        inital = [0] * answer
        for i in range(1, answer):
            while ms and temperatures[ms[-1]] < temperatures[i]:
                inital[ms.pop()] = i - ms[-1]
            ms += i,
        return inital
        
        