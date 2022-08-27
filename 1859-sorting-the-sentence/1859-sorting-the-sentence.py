class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        w = s.split(" ")
        t = [0]*len(w)
        for i in range(0,len(w)):
            t[int(w[i][-1])-1] = w[i][0:-1]
        return ' '.join(t)


