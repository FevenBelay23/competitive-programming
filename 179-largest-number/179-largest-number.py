class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arranged_str = ''
        count = 0
        if len(nums) == 0: 
            return ""
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                k, l = str(nums[i]), str(nums[j])
                if(int(l+k) > int(k+l)): 
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == 0: 
            return '0'
        while count < len(nums): 
            arranged_str  += str(nums[count])
            count+=1               
        return arranged_str 
        