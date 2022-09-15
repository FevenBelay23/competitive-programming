class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Queue = deque([(nums[0],0)])
        score = nums[0]
        for i in range(1, len(nums)):
            while Queue and Queue[0][1]<i-k:
                Queue.popleft()
            score = nums[i]+Queue[0][0]
            while Queue and score>=Queue[-1][0]:
                Queue.pop()
            Queue.append((score,i))
        return score