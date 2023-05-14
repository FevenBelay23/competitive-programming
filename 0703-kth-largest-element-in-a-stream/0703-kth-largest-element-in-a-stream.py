class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mini = []
        for i in nums:
            self.add(i)
        

    def add(self, val: int) -> int:
        if len(self.mini) < self.k:
            heappush(self.mini, val)
        else:
            if val > self.mini[0]:
                heappop(self.mini)
                heappush(self.mini, val)
        return self.mini[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)