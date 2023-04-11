class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_sort = sorted(nums)
        List = []
        for i in range(n):
            if nums_sort[i] == target:
                List.append(i)
        return List
