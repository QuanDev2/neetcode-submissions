class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMax(split_nums: List[int]) -> int:
            two, one = 0, 0
            for n in split_nums:
                two, one = one, max(two + n, one)
            return one

        if len(nums) == 1:
            return nums[0]
        return max(robMax(nums[1:]), robMax(nums[:len(nums)-1]))
