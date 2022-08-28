class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_indices_list = []
        t_Count = 0
        smaller = 0
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target: 
                t_Count += 1
        
        while t_Count > 0:
            target_indices_list.append(smaller)
            smaller += 1
            t_Count -= 1
        
        return target_indices_list
        