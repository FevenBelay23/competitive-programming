class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0
        for k in range(-n + 1, n):
            for l in range(-n + 1, n):
                overlap = 0
                for i in range(max(0, -k), min(n, n - k)):
                    for j in range(max(0, -l), min(n, n - l)):
                        overlap += img1[i + k][j + l] & img2[i][j]
                max_overlap = max(max_overlap, overlap)
        return max_overlap