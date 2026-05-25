class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            runningProd = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                runningProd *= nums[j]
            res.append(runningProd)
            
        return res