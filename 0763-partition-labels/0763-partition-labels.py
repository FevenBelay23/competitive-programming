class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last= {}
        stack= []
        temp=0
        end = 0
        total= 0 
        for i,j in enumerate(s):
            last[j] =i
        while end < len(s):
            end = max(end,last[s[temp]])
            start = temp
            while temp < end:
                end = max(end,last[s[temp]])
                temp += 1
            if temp == end:
                stack.append(end-start+1)
                total += stack[-1]
                if total == len(s):
                    return stack
                temp += 1