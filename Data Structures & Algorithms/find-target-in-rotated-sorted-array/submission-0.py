class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [2,3,4,5,1] >
        # [3,4,5,1,2] >
        # [1,2,3,4,5] --
        # [4,5,1,2,3] 
        # [5,1,2,3,4] 
        # if mid < right => right half is sorted
        # for mid, check if target is in the sorted half
        # else, search the other half
        i, j = 0, len(nums)-1
        while i <= j:
            m = (i+j) // 2
            if target == nums[m]:
                return m
            if nums[m] < nums[j]: # right half is sorted
                if target > nums[m] and target <= nums[j]:
                    i = m+1
                else:
                    j = m-1
            else: # left half is sorted
                if nums[i] <= target and target < nums[m]:
                    j = m-1
                else:
                    i = m+1
        return -1