class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        List=[0]*len(nums)
        j= 1
        k=0
        temp=0
        count = 0
        for i in nums:
            if i == 0:
                temp= k
                k+=1
                count+=1
                if count >1:
                    return([0]*len(nums))
                continue
            k+=1
            j = j*i
        for i in range(len(nums)):
            if nums[i] == 0:
                List = [0]*len(nums)
                List[temp] = j
                return List
            List[i] = j//nums[i]
        return List