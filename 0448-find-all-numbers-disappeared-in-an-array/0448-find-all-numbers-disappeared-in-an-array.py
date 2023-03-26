class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        answer = []
        for i in range(n):
            if nums[i] != i + 1:
                answer.append(i + 1)
        
        return answer