class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        dictionary = defaultdict(int)
        heap = [[0, i] for i in range(n)]
        heapify(heap)
        for first, last in meetings:
            for i in range(n):
                if heap[i][0] <= first:
                    heap[i][0] = 0
            heapify(heap)
            if heap[0][0] <= first:
                dictionary[heap[0][1]] += 1
                heappushpop(heap, [last, heap[0][1]])
            else:
                dictionary[heap[0][1]] += 1
                heappushpop(heap, [last - first + heap[0][0], heap[0][1]])
        temp = dictionary[0]
        ans = 0
        for key in dictionary:
            if temp < dictionary[key]:
                ans = key
                temp = dictionary[key]
            elif temp == dictionary[key]:
                ans = min(key, ans)
        return ans