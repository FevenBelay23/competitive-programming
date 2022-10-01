class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap) >= 2:
            f= -heapq.heappop(heap)
            s= -heapq.heappop(heap)
            if f==s:
                continue
            else:
                temp = f-s
                heapq.heappush(heap, -temp)
        if heap:
            return -heap[0]
        return 0