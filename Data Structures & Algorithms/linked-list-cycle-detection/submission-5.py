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
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next

        # return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
"""
Time: O(n)
space: O(1) using 2 pointers, speed = 1 and 2
"""
   



