# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Dummy node acts as the starting point for the merged list
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists, picking the smaller value each time
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    # If one list is exhausted, attach the remainder of the other list
    if l1 is not None:
        current.next = l1
    else:
        current.next = l2
        
    # Return the head of the merged list
    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(mergeTwoLists(l1, l2))

            lists = mergedLists

        return lists[0]