class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(float('-inf'))
        area_max = 0
        stack = []
        
        for i in range(len(heights)):
            curr_lb = i - 1
            while stack and heights[stack[-1][0]] >heights[i]:
                val = stack.pop()
                curr_lb = val[1]
                right = i
                area_max = max(area_max, heights[val[0]] * (right - curr_lb - 1))
                
            stack.append((i, curr_lb))
                
        return area_max