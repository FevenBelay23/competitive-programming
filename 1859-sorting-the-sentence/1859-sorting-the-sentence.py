class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited= s[::-1].split() 
        splited.sort()     
        answer = []  
        for word in splited:  
            answer.append(word[1:][::-1]) 
        return " ".join(answer) 


