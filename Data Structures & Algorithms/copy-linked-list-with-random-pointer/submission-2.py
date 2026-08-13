"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        finder = {}

        node = head
        while node:
            # FIX: Use the actual node object as the key, not node.val
            finder[node] = Node(node.val)
            node = node.next

        root = Node(0)

        node = head
        new = root
        while node:
            # FIX: Look up the copy using the node object
            new.next = finder[node]
            
            if node.random:
                # FIX: Look up the random copy using the random node object
                new.next.random = finder[node.random]

            new = new.next
            node = node.next


        return root.next