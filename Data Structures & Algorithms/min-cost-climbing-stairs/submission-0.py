class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # when you're at [i], the minCost to get there is cost[i] + cost[where you came from i-1/ i-2]
        memoi = {}
        n = len(cost)
        def getMinCostAt(i) -> int:
            if i < 0:
                return 0;
            if i not in memoi:
                memoi[i] = min(cost[i] + getMinCostAt(i-1), cost[i] + getMinCostAt(i-2))
            
            return memoi[i]

        return min(getMinCostAt(n-1), getMinCostAt(n-2))