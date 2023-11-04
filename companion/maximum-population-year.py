class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        change = [0] * 101
        for birth, death in logs:
            change[birth - 1950] += 1
            if death < 2050:
                change[death - 1950] -= 1
        population = 0
        current = 0
        total = 0
        earliest = 0
        for i in range(101):
            current += change[i]
            if current > population:
                population = current
                earliest = i + 1950
            total += current
        return earliest






