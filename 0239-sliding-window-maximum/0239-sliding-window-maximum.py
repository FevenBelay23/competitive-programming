class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        win = deque()
        left = 0
        right = 0
        
        while right < len(nums):
            while win and nums[win[-1]] < nums[right]:
                win.pop()
            win.append(right)
            
            if left > win[0]:
                win.popleft()
                
            if (right + 1) >= k:
                ans.append(nums[win[0]])
                left +=1
            right += 1
            
        return ans
            
            
        