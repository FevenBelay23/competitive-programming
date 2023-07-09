class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(first, second):
            while second:
                first, second = second, first % second
            return first
        counter = Counter(deck)
        counts = list(counter.values())
        x = counts[0]
        for i in counts[1:]:
            x = gcd(x, i)
        return x >= 2