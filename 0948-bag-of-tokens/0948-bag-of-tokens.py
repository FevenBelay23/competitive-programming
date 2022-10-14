class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        i=0
        j=len(tokens)-1
        score=0
        Max=0
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                score +=1
                i+=1
            elif score>0 :
                score -=1
                power+=tokens[j]
                j-=1
            else:
                return Max
            if Max<score:
                Max=score
        return Max