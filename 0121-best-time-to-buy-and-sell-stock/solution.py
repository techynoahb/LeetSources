class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cost = 0
        profit = 0
        minCost = prices[0]
        n = len(prices)

        for i in range(n):
            cost = prices[i] - minCost
            profit = max(profit, cost)
            minCost = min(minCost, prices[i])

        return profit
