class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curr_max, curr_min = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            candidates = (n, curr_max * n, curr_min * n)
            curr_max = max(candidates)
            curr_min = min(candidates)
            res = max(res, curr_max)
        return res