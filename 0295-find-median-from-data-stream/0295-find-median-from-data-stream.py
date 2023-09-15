class MedianFinder:

    def __init__(self):
        self.large = [] 
        self.small = [] 
        

    def addNum(self, num: int) -> None:
        if not self.large or num <= -self.large[0]:
            heapq.heappush(self.large, -num)
        else:
            heapq.heappush(self.small, num)
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (-self.large[0] + self.small[0]) / 2
        else:
            return -self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()