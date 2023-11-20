class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices:
            return 0
        first_buy = [float('-inf')] * n
        first_sell = [0] * n
        second_buy = [float('-inf')] * n
        second_sell = [0] * n
        first_buy[0] = -prices[0]
        first_sell[0] = 0
        second_buy[0] = -prices[0]
        second_sell[0] = 0
        for i in range(1, n):
            first_buy[i] = max(first_buy[i-1], -prices[i])
            first_sell[i] = max(first_sell[i-1], first_buy[i-1] + prices[i])
            second_buy[i] = max(second_buy[i-1], first_sell[i-1] - prices[i])
            second_sell[i] = max(second_sell[i-1], second_buy[i-1] + prices[i])
        return second_sell[-1]