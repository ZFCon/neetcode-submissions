# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        length = 0

        node = head
        while node:
            node = node.next
            length += 1
        
        nn = length - n

        node = head
        prevoiuse = None
        counter = 0
        while node:
            if counter == nn:
                if not prevoiuse:
                    head = node.next
                    break
                else:
                    prevoiuse.next = node.next
            prevoiuse = node
            node = node.next
            counter += 1

        return head