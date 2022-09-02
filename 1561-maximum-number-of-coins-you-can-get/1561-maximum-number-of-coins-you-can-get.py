class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        i = 0
        j = len(piles)-2
        answer = 0
        while i<j:
            answer += piles[j]
            i += 1
            j -= 2
        return answer  