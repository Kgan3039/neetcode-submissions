class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        output = 0

        while sell < len(prices):
            tempOutput = 0
            if prices[sell] > prices[buy]:
                tempOutput = prices[sell] - prices[buy]
                output = max(output, tempOutput)
            else:
                buy = sell
            sell += 1

        return output



        



        