class Solution:
    def rob(self, nums: List[int]) -> int:
        memoi = {}
        def maxRob(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memoi:
                memoi[i] = max(maxRob(i-1), nums[i] + maxRob(i-2))
            return memoi[i]

        return maxRob(len(nums)-1)