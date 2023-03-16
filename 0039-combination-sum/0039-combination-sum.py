class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combination(current , nums_sum , index):
            if nums_sum == target:
                result.append(current[:])
                return
            if index == len(candidates) or (target - nums_sum) < candidates[index]:
                return

            current.append(candidates[index])
            combination(current , nums_sum + candidates[index] , index)
            current.pop()
            combination(current , nums_sum, index +1)
            
        candidates.sort()
        combination([],0,0)
        return result
            
           
                     
        