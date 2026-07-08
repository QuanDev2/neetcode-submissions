class Solution:
    def climbStairs(self, n: int) -> int:
        memoi = defaultdict(int)
        def dfs(steps: int) -> int:
            if steps == n:
                return 1
            if steps > n:
                return 0
            if steps in memoi:
                return memoi[steps]
            
            memoi[steps] = dfs(steps+1)+ dfs(steps + 2)
            
            return memoi[steps]

        return dfs(0)