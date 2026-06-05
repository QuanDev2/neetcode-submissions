# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time: O(n)
space: O(n)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            if visited and curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False
