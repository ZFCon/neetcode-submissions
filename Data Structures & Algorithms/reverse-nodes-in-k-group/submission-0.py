# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        potato_head = head
        counter = k
        while counter:
            if not potato_head: return head  # 1. ADDED: Stop and return if we run out of nodes before hitting k
            potato_head = potato_head.next
            counter -= 1

        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list
        snake_head = None
        counter = k
        while counter:
            if counter == k:
                snake_head = curr
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward
            counter -= 1
        
        # 2. CHANGED: Call the function on the rest of the list instead of just attaching potato_head
        snake_head.next = self.reverseKGroup(potato_head, k) 
        
        return prev  # prev is the new head of the reversed list