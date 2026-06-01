class Solution:
    # nums = [-1,0,2,4,6,8], i=0; j=5
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (j+i) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1