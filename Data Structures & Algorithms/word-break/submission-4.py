class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # for every s[i], check all the words w in wordDict to see if we can fit w from i-th pos onward
        # dp[i] = true => can build s[:i] using words from dict
        # return dp[-1]
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for w in wordDict:
                if not dp[i]:
                    continue
                lenW = len(w)
                if i+lenW <= n and not dp[i+lenW] and s[i:i+lenW] == w:
                    dp[i+lenW] = True
                    print(dp)
        return dp[-1]
