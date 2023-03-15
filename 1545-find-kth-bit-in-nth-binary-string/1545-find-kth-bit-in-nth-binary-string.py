class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        half = ((2**n) )// 2
        
        if k == 1:
            return "0"
        
        if k < half:
            return self.findKthBit(n-1 , k)
        elif k > half:
            return str(1 - int(self.findKthBit(n - 1 , (2**n) - k)))
        else:
            return "1"
        
        
        
