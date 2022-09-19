class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        fmax=0
        lmax=0
        temp=0
        nos = nums[:] 
        for i in range(1,len(nums)):
            nos[i]+=nos[i-1] 
        nos.insert(0,0) 
        for i in range(firstLen+1, len(nos)-secondLen+1): 
            fsum = nos[i+secondLen-1] - nos[i-1]
            fmax = max(fmax, nos[i-1]-nos[i-1-firstLen])
            temp = max(temp,fsum+fmax)
        for i in range(secondLen+1, len(nos)-firstLen+1): 
            lsum = nos[i+firstLen-1] - nos[i-1]
            lmax = max(lmax, nos[i-1]-nos[i-1-secondLen])
            temp = max(temp,lsum+lmax)
        return temp