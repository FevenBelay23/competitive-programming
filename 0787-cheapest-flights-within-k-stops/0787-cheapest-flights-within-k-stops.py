class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0
        for i in range(k + 1):
            curr_price = price.copy()
            for x , y , z in flights:
                if price[x] == float("inf"):
                    continue
                if price[x] + z < curr_price[y]:
                    curr_price[y] = price[x] + z 
            price = curr_price
            
        if price[dst] == float("inf"):
            return -1
        else:
            return price[dst]

        