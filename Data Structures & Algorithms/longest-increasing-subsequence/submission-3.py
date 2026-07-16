class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n+1) # dp[i]: holds the LIS of string s[:i]
        # [9,1,3,7]
        # [1,1,2,3]
        res = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        #             res = max(res, dp[i])
        # return res
        memoi = {}
        def lisUpTo(i: int) -> int:
            nonlocal res

            if i in memoi:
                return memoi[i]

            memoi[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    memoi[i] = max(memoi[i], lisUpTo(j) + 1)
                    res = max(memoi[i], res)
            return memoi[i]
        
        for i in range(1, n):
            lisUpTo(i)
        return res


