class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        start = Next = float('inf')
        for num in nums:
            if num <= start:
                start = num
            elif num <= Next:
                Next = num
            else:
                return True
        return False