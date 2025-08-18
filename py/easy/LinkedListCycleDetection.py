from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow, fast = head, head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
