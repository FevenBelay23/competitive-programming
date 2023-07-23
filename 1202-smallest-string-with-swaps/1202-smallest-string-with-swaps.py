class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(related, x):
            if related[x] != x:
                related[x] = find(related, related[x])
            return related[x]

        def union(related, rank, x, y):
            for_x = find(related, x)
            for_y = find(related, y)
            if for_x != for_y:
                if rank[for_x] < rank[for_y]:
                    related[for_x] = for_y
                elif rank[for_x] > rank[for_y]:
                    related[for_y] = for_x
                else:
                    related[for_y] = for_x
                    rank[for_x] += 1
        n = len(s)
        related = [i for i in range(n)]
        rank = [0] * n
        for i in pairs:
            union(related, rank, i[0], i[1])
        group = defaultdict(list)
        for i in range(n):
            group[find(related, i)].append(i)
        result = list(s)
        for i in group.values():
            lexi = sorted(s[i] for i in i)
            for i, char in zip(i, lexi):
                result[i] = char
        return ''.join(result)

        