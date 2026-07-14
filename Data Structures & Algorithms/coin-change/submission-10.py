class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0
        # amount = 3
        # [0, !, !, !]
        for amt in range(1, amount+1):
            for coin in coins:
                if coin > amt:
                    continue
                minCoins[amt] = min(minCoins[amt], minCoins[amt - coin] + 1)
        
        return -1 if minCoins[-1] > amount else minCoins[-1]