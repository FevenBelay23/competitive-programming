class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(pair, left, right):
            if len(pair) == 2 * n:
                ans.append(pair)
                return
            if left < n:
                backtrack(pair + '(', left + 1, right)
            if right < left:
                backtrack(pair + ')', left, right + 1)
        ans = []
        backtrack('', 0, 0)
        return ans