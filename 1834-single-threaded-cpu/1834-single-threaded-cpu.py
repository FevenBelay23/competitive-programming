class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        taskList = [(enqueueTime, processingTime, index) for index, (enqueueTime, processingTime) in enumerate(tasks)]
        taskList.sort()
        heap = []  
        total = 0
        result = []
        i = 0
        while i < n or heap:
            if not heap:
                total = max(total, taskList[i][0])  
            while i < n and taskList[i][0] <= total:
                heapq.heappush(heap, (taskList[i][1], taskList[i][2]))
                i += 1
            processingTime, index = heapq.heappop(heap)
            total += processingTime
            result.append(index)
        return result




