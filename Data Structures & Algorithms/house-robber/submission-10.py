class Solution:
    def rob(self, nums: List[int]) -> int:
        # memoi = {}
        # def maxRob(i: int) -> int:
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
        #     if i not in memoi:
        #         memoi[i] = max(maxRob(i-1), nums[i] + maxRob(i-2))
        #     return memoi[i]

        # return maxRob(len(nums)-1)
        n = len(nums)
        # tab = [0] * n

        # tab[0] = nums[0]
        # if n == 1:
        #     return tab[0]

        # tab[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     tab[i] = max(tab[i-1], tab[i-2] + nums[i])

        # return tab[-1]

        if n == 1:
            return nums[0]
        robTwo, robOne = nums[0], max(nums[1], nums[0])

        for i in range(2, n):
            currRob = max(robOne, robTwo + nums[i])
            robTwo, robOne = robOne, currRob
        return robOne

