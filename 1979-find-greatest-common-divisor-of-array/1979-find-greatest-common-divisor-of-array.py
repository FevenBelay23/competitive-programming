class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        gcd = self.gcd(smallest, largest)
        return gcd
    
    def gcd(self, first: int, second: int) -> int:
        while second:
            first, second = second, first % second
        return first