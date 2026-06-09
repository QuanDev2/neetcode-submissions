"""
For each day, ask if today's price is the best buying price.
Compare today's price to best buying price so far.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        profit = 0
        for i in range(len(prices)-1):
            # if we sell the stock today, when was the best time to buy
            bestBuy = min(bestBuy, prices[i])
            profit = max(profit, prices[i+1] - bestBuy)
        
        return profit