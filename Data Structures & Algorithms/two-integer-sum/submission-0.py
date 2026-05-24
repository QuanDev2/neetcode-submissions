# O(n) space and time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # traverse nums
        # for each num, store complement as key, idx as value(s)
        # we will find one that matches one of the keys
        # the current idx is always the larger num
        # => use min of value list
        
        comps = {}
        for idx, num in enumerate(nums):
            if num in comps:
                return [comps[num], idx]
            else:
                comps[target - num] = idx
        return [];