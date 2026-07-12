class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Goal: arrive at top of stairs, meaning n = 3, then we need to return cost to arrive at 4. 
        # cost to arrive at 4 = min(cost to arrive at 3 - then take cost[3], cost to arrive at 2 - then take cost[2])
        n = len(cost)
        # memoi = {}
        # def getMinCostToArriveAt(i) -> int:
        #     if i < 0:
        #         return 0;
        #     if i not in memoi:
        #         memoi[i] = min(getMinCostToArriveAt(i-1) + cost[i-1], getMinCostToArriveAt(i-2) + cost[i-2])
            
        #     return memoi[i]

        # return getMinCostToArriveAt(n)

        ### tabulation
        tab = [0] * (n+1)
        for i in range(2, n+1):
            tab[i] = min(tab[i-1] + cost[i-1], tab[i-2] + cost[i-2])
        return tab[-1]
