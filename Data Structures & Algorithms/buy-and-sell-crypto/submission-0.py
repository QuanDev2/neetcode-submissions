class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        bestBuy = prices[0]
        profit = 0
        for i in range(len(prices)-1):
            # if we sell the stock today, when was the best time to buy
            bestBuy = min(bestBuy, prices[i])
            profit = max(profit, prices[i+1] - bestBuy)
        
        return profit