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

        """
        Optimal: with every n, instead of asking if it could be the start, ask if it should NOT be the start. It should not when n-1 exists.
        """
        def longestConsecutive(self, nums: List[int]) -> int:       
            # nums_set = set(nums)
            # cnt = 0
            # for n in nums:
            #     if n-1 in nums_set:
            #         continue
                
            #     curr_cnt = 1
            #     while n+1 in nums_set:
            #         curr_cnt += 1
            #         n += 1
            #     cnt = max(cnt, curr_cnt)

            # return cnt
                    numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
