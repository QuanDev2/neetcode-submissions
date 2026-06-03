class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [2,3,4,5,1] >
        # [3,4,5,1,2] >
        # [1,2,3,4,5] 
        # [4,5,1,2,3] 
        # [5,1,2,3,4] 
        # observation: if min < right => right half is sorted => pivot is on left half. pivot is min
        i, j = 0, len(nums)-1
        while i < j:
            m = (i+j) // 2
            if nums[m] > nums[j]:
                # min is on right half -> move right
                i = m+1
            else:
                j = m
            
        return nums[i]
        