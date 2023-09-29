class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        column = len(dungeon[0])
        dp = [[0] * column for _ in range(row)]
        for i in range(row-1 , -1 , -1):
            for j in range(column-1, -1 , -1):
                if i == row - 1 and j == column - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == row - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == column - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
                     