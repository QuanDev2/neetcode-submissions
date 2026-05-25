"""
Assume that nums[i] is the start of the longest, check n+1;
Time: O(n^2)
Space: O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:       
        cnt = 0
        for n in nums:
            longest  = set()
            longest.add(n)
            while n+1 in nums:
                longest.add(n+1)
                n += 1
            if len(longest) > cnt:
                cnt = len(longest)
        return cnt