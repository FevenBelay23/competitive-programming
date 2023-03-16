class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
        result = []
        def combination(current, nums_sum, index):
            
            if nums_sum == target:
                result.append(current[:])
                return
            if index >= len(candidates):
                return
            if nums_sum > target:
                return
            
            for i in range(index, len(candidates)):             
                if i > index and candidates[i] == candidates[i-1]:
                        continue
                current.append(candidates[i])
                nums_sum += candidates[i]
                combination(current, nums_sum, i + 1)
                end = current.pop()
                nums_sum -= end
                    
        
        candidates.sort()
        combination([], 0, 0)
        return result
        