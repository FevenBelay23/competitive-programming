class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        coordinate = [i for i in range(n)]
        step = [0] * n
        count = n
        def find(x):
            if coordinate[x] != x:
                coordinate[x] = find(coordinate[x])
            return coordinate[x]
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if step[root_x] < step[root_y]:
                    coordinate[root_x] = root_y
                elif step[root_x] > step[root_y]:
                    coordinate[root_y] = root_x
                else:
                    coordinate[root_y] = root_x
                    step[root_x] += 1
                nonlocal count
                count -= 1
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        return n - count

        