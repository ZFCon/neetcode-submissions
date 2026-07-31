class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        n = 0
        node = head
        finder = {}

        while node:
            finder[n] = node
            node = node.next
            n += 1

        node = head

        for i in range(1, (n//2)+1):
            new = finder[n-i]
            new.next = None
            node.next = new

            if n - i == i:
                break

            new2 = finder[i]
            new2.next = None
            new.next = new2
            node = new2