class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num=list(num)
        stack=[]
        i=0
        for i in num:             
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1 
            if i!='0' or stack: 
                stack.append(i) 
        if k!=0:
            stack=stack[:-k]
        if not stack:
            return '0'
        return ''.join(stack)