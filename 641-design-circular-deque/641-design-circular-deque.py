class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max= k 
        self.queue = deque([])

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.max:
            self.queue.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue)<self.max:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.popleft()
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        else:
            return -1 


    def getRear(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        else:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue)==self.max
     


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()