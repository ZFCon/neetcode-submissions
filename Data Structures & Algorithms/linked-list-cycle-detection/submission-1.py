# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        p1 = head
        p2 = head.next

        while p1.next:
            if p1 == p2:
                return True

            p1 = p1.next
            if p2 and p2.next:
                p2 = p2.next.next

        return False