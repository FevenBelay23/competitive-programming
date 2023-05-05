class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(position, current, result):
            if len(current) != len(set(current)):
                return result
            result = max(result, len(current))
            for i in range(position, len(arr)):
                result = backtrack(i + 1, current + arr[i], result)
            return result

        answer = backtrack(0, "", 0)
        return answer