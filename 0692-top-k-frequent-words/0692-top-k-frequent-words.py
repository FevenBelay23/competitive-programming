class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = []
        for i, count in count.items():
            heapq.heappush(heap, (-count, i))
        frequent = [heapq.heappop(heap)[1] for _ in range(k)]
        return frequent