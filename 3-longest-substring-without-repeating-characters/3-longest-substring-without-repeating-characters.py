class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        temp= 0
        while(i<len(s) and j<len(s)):
            if len(set(s[i:j+1]))==len(s[i:j+1]):
                temp = max(temp,len(s[i:j+1]))
                j+=1
            else:i+=1
        return temp