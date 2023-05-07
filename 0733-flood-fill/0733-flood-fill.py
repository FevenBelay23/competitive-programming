class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, row, column, old, new):
            if image[row][column] != old:
                return
            image[row][column] = new
            if row > 0:
                dfs(image, row-1, column, old, new)
            if row < len(image) - 1:
                dfs(image, row+1, column, old, new) 
            if column > 0:
                dfs(image, row, column-1, old, new) 
            if column < len(image[0]) - 1:
                dfs(image, row, column+1, old, new) 
        if image[sr][sc] == color:
            return image
        dfs(image, sr, sc, image[sr][sc], color)
        return image

    