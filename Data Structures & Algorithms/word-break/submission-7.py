class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # for every s[i], check all the words w in wordDict to see if we can fit w from i-th pos onward
        # dp[i] = true => can build s[:i] using words from dict (excluding char s[i])
        # return dp[-1]
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            if not dp[i]:
                continue
            for w in wordDict:
                lenW = len(w)
                if s[i:i+lenW] == w:
                    dp[i+lenW] = True
        return dp[-1]