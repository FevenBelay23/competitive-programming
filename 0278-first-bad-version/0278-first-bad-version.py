# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high = 1,n
        bad=n
        while low <= high:
            mid = (high+low)//2
            if isBadVersion(mid):
                bad = min(mid,bad)
                high = mid-1
            else:
                low = mid+1
        return bad
        