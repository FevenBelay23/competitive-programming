class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        temp = [[] for _ in range(n)]
        for i , j in roads:
            temp[i].append(j)
            temp[j].append(i)
        max_network_rank= 0
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the rank of the pair (u, v)
                rank = len(temp[i]) + len(temp[j])
                if j in temp[i]:
                    rank -= 1
                max_network_rank = max(max_network_rank, rank)
        return max_network_rank
