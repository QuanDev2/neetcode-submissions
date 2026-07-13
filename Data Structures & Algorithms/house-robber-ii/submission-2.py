class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMax(split_nums: List[int]) -> int:
            n = len(split_nums)
            if n == 1:
                return split_nums[0]

            dp = [0] * n
            dp[0] = split_nums[0]
            dp[1] = max(split_nums[0], split_nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + split_nums[i])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        return max(robMax(nums[1:]), robMax(nums[:-1]))
