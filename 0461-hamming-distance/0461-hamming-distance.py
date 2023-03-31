class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = x ^ y
        count = 0
        while dis:
            count += dis & 1
            dis >>= 1
        
        return count