class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-j for j in piles]
        heapify(heap)
        for i in range(k):
            current = -heappop(heap)
            new = current - (current // 2)
            heappush(heap, -new)
        return -sum(heap)