class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        change = [n] * n  
        same = [n] * n  
        change[0] = 1 
        same[0] = 0  
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                same[i] = min(same[i], same[i - 1])
                change[i] = min(change[i], change[i - 1] + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                same[i] = min(same[i], change[i - 1])
                change[i] = min(change[i], same[i - 1] + 1)
        return min(change[-1], same[-1])