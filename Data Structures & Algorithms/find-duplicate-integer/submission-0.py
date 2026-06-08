"""
we can think of this array being a linked list.
each array element is the pointer to the next node.
This is possible because all the numbers are unique except the repeated one.

First, use 2 pointers (fast and slow) to find the meet up point.
Then move slow back to start, and start moving them.
Where they meet again is the entry point to the cycle -> the duplicate value
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow