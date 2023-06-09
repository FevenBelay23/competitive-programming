class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        for _ in range(k - 1):
            _, row, column = heapq.heappop(heap)
            if column < n - 1:
                heapq.heappush(heap, (matrix[row][column + 1], row, column + 1))
        return heap[0][0]