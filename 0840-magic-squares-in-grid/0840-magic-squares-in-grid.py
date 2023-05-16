class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magicSquareInGrid(subgrid):
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = subgrid[i][j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            total = subgrid[0][0] + subgrid[0][1] + subgrid[0][2]
            for i in range(3):
                if sum(subgrid[i]) != total:
                    return False
            for j in range(3):
                if sum(subgrid[i][j] for i in range(3)) != total:
                    return False
            if (subgrid[0][0] + subgrid[1][1] + subgrid[2][2]) != total or (subgrid[0][2] + subgrid[1][1] +subgrid[2][0]) != total:
                return False
            return True
        count = 0
        row, column = len(grid), len(grid[0])
        for i in range(row - 2):
            for j in range(column - 2):
                subgrid = [grid[x][j:j + 3] for x in range(i, i + 3)]
                if magicSquareInGrid(subgrid):
                    count += 1
        return count


        