class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack1.append(val)
        if len(self.stack2) == 0:
            self.stack2.append(val)
        else:
            self.stack2.append(min(val, self.stack2[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack1.pop()
        self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]
   
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()