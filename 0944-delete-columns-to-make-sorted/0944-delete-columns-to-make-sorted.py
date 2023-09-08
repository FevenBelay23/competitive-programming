class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = []
        for column in range(len(strs)-1):
            for row in range(len(strs[0])):
                if (strs[column][row] > strs[column + 1][row]):
                    count.append(row)
        return len(set(count))
        