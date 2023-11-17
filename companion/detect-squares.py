class DetectSquares:

    def __init__(self):
        self.total = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        i, j = point
        self.total[(i, j)] += 1
        self.points.append((i, j))

    def count(self, point: List[int]) -> int:
        i, j = point
        result = 0
        for px, py in self.points:
            if px != i and py != j and abs(px - i) == abs(py - j):
                result += self.total[(px, j)] * self.total[(i, py)]
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)