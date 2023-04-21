class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_Amt = 0
        while i < j:
            current_area = min(height[i], height[j]) * (j - i)
            max_Amt = max(max_Amt, current_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_Amt