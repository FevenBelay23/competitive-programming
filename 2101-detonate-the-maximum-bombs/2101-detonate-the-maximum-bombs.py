class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        detonation = defaultdict(list)
        count = len(bombs)
        for i in range(count):
            k, l, m = bombs[i]
            for j in range(i+1, count):
                a, b, c = bombs[j]
                distance = (a - k) ** 2 + (b - l) ** 2
                if distance <= m ** 2:
                    detonation[i].append(j)
                if len(detonation[i]) == count - 1:
                    return count
                if distance <= c ** 2:
                    detonation[j].append(i)
                if len(detonation[j]) == count - 1:
                    return count
        damage = [0] * count
        visited = [0] * count
        def dfs(i):
            damage[i] = 1
            visited[i] = 1
            for j in detonation[i]:
                if not visited[j]:
                    damage[j] = dfs(j)
                    visited[j] = 1
                    damage[i] += damage[j]
            return damage[i]
        maxDetonated = 0
        for i in range(count):
            visited = [0] * count
            if not damage[i]:
                damage[i] = dfs(i)
            maxDetonated = max(maxDetonated, damage[i])
        return maxDetonated