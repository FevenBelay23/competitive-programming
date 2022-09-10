class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num=sorted(citations)
        j=len(num)-1
        k=0
        for i in range(len(num)):
            if i+1<=num[i] and j-i+1>=num[i]:
                k=max(num[i],k)
            elif i+1<= num[i] and j-i+1<num[i]:
                k=max(k,j-i+1)
            elif i+1>num[i] and j-i+1>=num[i]:
                k=max(k, num[i])
        return k