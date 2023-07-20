class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = {}
        for i in adjacentPairs:
            j, k = i
            pairs.setdefault(j, []).append(k)
            pairs.setdefault(k, []).append(j)
        for num, neighbors in pairs.items():
            if len(neighbors) == 1:
                start = num
                break
        n = len(adjacentPairs) + 1
        result = [start]
        previous = None
        current = start
        for _ in range(n - 1):
            neighbors = pairs[current]
            for neighbor in neighbors:
                if neighbor != previous:
                    result.append(neighbor)
                    previous, current = current, neighbor
                    break
        return result



