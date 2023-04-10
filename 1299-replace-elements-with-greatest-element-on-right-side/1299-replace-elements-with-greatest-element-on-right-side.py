class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1 
        for i in range(len(arr) - 1, -1, -1):
            idx = arr[i]
            arr[i] = right_max
            right_max = max(right_max, idx)
        return arr
        