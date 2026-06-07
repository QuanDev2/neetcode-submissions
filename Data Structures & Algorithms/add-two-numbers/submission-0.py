# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
walk both lists, add number by number.
remember the carry.
do it while c1 exist or c2 exist or carry non zero
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        c1, c2, carry = l1, l2, 0
        while c1 or c2 or carry > 0:
            num1 = c1.val if c1 else 0
            num2 = c2.val if c2 else 0
            sum = num1 + num2 + carry
            digit = sum % 10
            carry = sum // 10
            newNode = ListNode(digit)
            prev.next = newNode
            prev = prev.next
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return dummy.next