class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # minCoins = [float('inf')] * (amount + 1)
        # minCoins[0] = 0
        # # amount = 3
        # # [0, !, !, !]
        # for amt in range(1, amount+1):
        #     for coin in coins:
        #         if coin > amt:
        #             continue
        #         minCoins[amt] = min(minCoins[amt], minCoins[amt - coin] + 1)
        
        # return -1 if minCoins[-1] > amount else minCoins[-1]
        memoi = {}
        def findMinCoin(amt: int) -> int: # find the min coin to make amt
            if amt == 0:
                return 0
            if amt not in memoi:
                memoi[amt] = float('inf')
                
                for c in coins:
                    if c > amt:
                        continue
                    memoi[amt] = min(memoi[amt], 1 + findMinCoin(amt - c))

            return memoi[amt]
        res = findMinCoin(amount)
        return res if res < float('inf') else -1

