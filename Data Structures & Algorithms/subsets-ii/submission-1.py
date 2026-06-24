class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,2]    

        """

 

        def dfs(start, path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        
        
        res = []
        nums.sort()
        dfs(0, [])

        return res