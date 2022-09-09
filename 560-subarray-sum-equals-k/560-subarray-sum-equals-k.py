class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        final = 0
        current = 0
        Lis = {current:1}
        for i in nums:
            current += i
            sub = current - k
            if sub in Lis: 
                final += Lis[sub]
            if current not in Lis:
                Lis[current] = 1
            else:
                Lis[current] += 1

        return final