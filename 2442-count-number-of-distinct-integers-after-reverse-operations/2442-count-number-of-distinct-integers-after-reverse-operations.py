class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            result.append(int(str(i)[::-1]))
        nums.extend(result)
        answer = len(set(nums))
        return answer
            
            
