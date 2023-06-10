class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        heap = []
        heapq.heapify(heap)
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                pair = nums1[i] + nums2[j]
                if len(heap) < k:
                    heapq.heappush(heap, (-pair, nums1[i], nums2[j]))
                else:
                    if pair > -heap[0][0]:
                        break
                    heapq.heappushpop(heap, (-pair, nums1[i], nums2[j]))
        result = []
        while heap and k > 0:
            _, num1, num2 = heapq.heappop(heap)
            result.append([num1, num2])
            k -= 1
        return result