class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i , answer = 0 , 0
        for house in houses:
            while (i+1 < len(heaters) and heaters[i] + heaters[i+1] <= house * 2):
                i += 1
            answer = max(answer , abs(heaters[i] - house))
        return answer
                
        