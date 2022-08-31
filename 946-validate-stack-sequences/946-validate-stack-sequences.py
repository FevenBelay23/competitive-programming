class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0 
        for i in pushed:
            stack.append(i)
            while (stack and stack[-1] == popped[j]):
                stack.pop(-1)
                j = j + 1
        if len(stack) == 0 :
            return True
        else:
            return False