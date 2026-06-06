# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2, prev = head, head, head
        for i in range(n):
            # don't worry about None 'cause n <= size
            p2 = p2.next

        # start advancing both
        while p2:
            prev, p1, p2 = p1, p1.next, p2.next

        if prev is p1:
            head = head.next

        prev.next = p1.next
        return head
