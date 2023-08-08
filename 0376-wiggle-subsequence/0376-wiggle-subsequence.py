class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        pos[0] = neg[0] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                pos[i] = neg[i - 1] + 1
                neg[i] = neg[i - 1]
            elif nums[i] < nums[i - 1]:
                neg[i] = pos[i - 1] + 1
                pos[i] = pos[i - 1]
            else:
                pos[i] = pos[i - 1]
                neg[i] = neg[i - 1]
        return max(pos[-1], neg[-1])