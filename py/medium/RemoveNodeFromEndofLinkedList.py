from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0:
            right = right.next  # type:ignore
            n -= 1
        while right:
            left = left.next  # type:ignore
            right = right.next  # type:ignore

        left.next = left.next.next  # type:ignore
        return dummy.next
