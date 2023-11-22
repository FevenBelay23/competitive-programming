class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        last = 0
        for i in arr:
            missing += i - last - 1
            if missing >= k:
                return last + (k - (missing - (i - last - 1)))
            last = i
        return arr[-1] + (k - missing)