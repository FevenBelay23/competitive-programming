class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        temp = 0
        while i <= len(prices) - 1:
            j = i
            while j < len(prices) - 1 and prices[j+1] - prices[j] ==-1:
                j += 1
            temp += (j - i) * (j - i + 1)// 2
            i = j + 1
        temp += len(prices)
        return temp