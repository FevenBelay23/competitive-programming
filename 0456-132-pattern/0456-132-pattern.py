class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ans = []
        add = -float('inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < add:
                return True
            while ans and nums[i] > ans[-1]:
                add = ans.pop()
            ans.append(nums[i])
        return False
        