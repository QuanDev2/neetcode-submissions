class Solution:
    def numDecodings(self, s: str) -> int:
        memoi = {}
        def dfs(i: int) -> int: # count ways of the s[i:] string
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i not in memoi:
                ways = 0
                ways += dfs(i+1)

                if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    ways += dfs(i+2)

                memoi[i] = ways
            return memoi[i]
        
        return dfs(0)
