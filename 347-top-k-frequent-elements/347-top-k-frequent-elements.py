class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        answer=[]
        for i,j in count.most_common(k):
            answer.append(i)
        return answer