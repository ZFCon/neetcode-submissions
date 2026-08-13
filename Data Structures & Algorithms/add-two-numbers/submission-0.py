# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node: ListNode) -> str:
            if not node.next:
                return str(node.val)

            return dfs(node.next) + str(node.val)
            

        number = list(str(int(dfs(l1))+int(dfs(l2))))

        root = ListNode(0)

        node = root
        while number:
            node.next = ListNode(int(number.pop()))

            node = node.next

        return root.next