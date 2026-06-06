# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find mid point using 2 pointers, split the list
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        
        p1, p2 = slow, slow.next
        p1.next = None
        
        # 2. reverse the 2nd half
        curr = p2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # now, prev will be the new head
        p2 = prev

        # 3. merge two lists
        p1 = head
        while p1 and p2:
            nxt1 = p1.next
            p1.next = p2
            p1 = nxt1

            nxt2 = p2.next
            p2.next = p1
            p2 = nxt2
