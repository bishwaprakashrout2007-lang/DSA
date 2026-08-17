class Solution:
    def rotateRight(self, head, k):
        # Empty list or single node
        if not head or not head.next:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # No actual rotation needed
        k = k % length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Node after new tail is the new head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head