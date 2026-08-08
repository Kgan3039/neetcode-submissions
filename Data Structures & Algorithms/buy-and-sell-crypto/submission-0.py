class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        best = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                best = max(best, profit)
            else: #if buy > sell
                buy = sell
            sell += 1
        
        return best




        