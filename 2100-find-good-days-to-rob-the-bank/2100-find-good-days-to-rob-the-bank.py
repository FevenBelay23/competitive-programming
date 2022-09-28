class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        f= len(security)   
        l = [0]*f
        r = [0]*f
        for i in range(1,f):
            if security[i-1] >= security[i]:
                l[i] = l[i-1] + 1
            if security[f-i-1] <= security[f-i]:
                r[f-i-1] = r[f-i] + 1    
        answer= []
        for i in range(f):
            if(l[i] >= time and r[i] >= time):
                answer.append(i)
        return answer