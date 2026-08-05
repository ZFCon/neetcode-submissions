# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        
        # Step 1: Iterate through all linked lists and extract their values
        for linked_list in lists:
            current = linked_list
            while current is not None:
                result.append(current.val)
                current = current.next
                
        # Step 2: Sort the combined list of values
        result.sort()
        
        # Step 3: Convert the sorted list back into a new linked list
        dummy = ListNode(0)
        current = dummy
        
        for val in result:
            current.next = ListNode(val)
            current = current.next
            
        # Return the head of the new sorted linked list (skipping the dummy node)
        return dummy.next