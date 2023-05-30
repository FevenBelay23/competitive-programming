class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(List, index):
            if len(List) <= 1:
                return List, index
            mid = len(List) // 2
            left, left_index = mergeSort(List[:mid], index[:mid])
            right, right_index = mergeSort(List[mid:], index[mid:])
            merged = []
            merged_index = []
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i] <= right[j]):
                    merged.append(left[i])
                    merged_index.append(left_index[i])
                    count[left_index[i]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    merged_index.append(right_index[j])
                    j += 1
            return merged, merged_index
    
        count = [0] * len(nums)
        _, index = mergeSort(nums, list(range(len(nums))))
        return count







