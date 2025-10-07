from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast:
            if fast == slow:
                return True
            slow = slow.next  # type:ignore
            fast = fast.next
            if fast:
                fast = fast.next

        return True
