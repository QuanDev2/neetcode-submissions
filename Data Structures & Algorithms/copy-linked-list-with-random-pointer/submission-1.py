"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
2 passes, first pass to construct the copy list, also build a hashmap of
{og nodes -> copy nodes}
2nd pass, get og random, look up copy random, point copy curr to copy random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1 means original, 2 means the copy ones
        curr1,curr2 = head, Node(head.val)
        copyNodes = {}
        head2 = curr2
        while curr1 and curr2:
            next2 = Node(curr1.next.val) if curr1.next else None
            curr2.next = next2
            # build random hashmap
            copyNodes[curr1] = curr2
            curr1, curr2 = curr1.next, curr2.next

            
        curr1, curr2 = head, head2
        print(copyNodes)
        while curr1 and curr2:
            curr2.random = copyNodes[curr1.random] if curr1.random else None
            curr1, curr2 = curr1.next, curr2.next

        return head2







