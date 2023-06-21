class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        for i in range(n - 1):
            comp = heights[i+1] - heights[i]
            if comp > 0:
                heapq.heappush(heap, comp)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return n - 1