class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndice = {}  
        for index, num in enumerate(nums):
            diff = target - num  
            if diff in numIndice:
                return [numIndice[diff], index]  
            numIndice[num] = index 
        return None 