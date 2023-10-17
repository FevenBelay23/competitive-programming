class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for i in range(n):
            small = large = temp = tot = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    small += 1
                elif rating[j] > rating[i]:
                    large += 1
            for k in range(i + 1, n):
                if rating[k] < rating[i]:
                    temp += 1
                elif rating[k] > rating[i]:
                    tot += 1
            count += (small * tot) + (large * temp)
        return count