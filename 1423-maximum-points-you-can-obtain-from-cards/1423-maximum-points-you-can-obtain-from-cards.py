class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        last= len(cardPoints)-1
        temp= k-1
        l= 0
        m= 0
        for i in range(k):
            l += cardPoints[i] 
        m= l
        while k:
            m-= cardPoints[temp]
            m+= cardPoints[last]
            temp -= 1
            last-= 1
            l = max(l,m)
            k-=1
        return l