from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        before_start, last = self.before_start_last_points(dummy, left, right)
        if not before_start or not last:
            print("before start or last is None")
            return

        start_node: ListNode | None = before_start.next
        after_last_node = last.next

        before_start.next = None
        last.next = None

        [start_reversed, tail] = self.reverse_and_return_head_tail(start_node)
        if not start_reversed or not tail:
            print("there is no start_reversed or tail")
            return
        tail.next = after_last_node
        before_start.next = start_reversed

        return dummy.next

    def before_start_last_points(
        self, dummy: ListNode, left: int, right: int
    ) -> List[ListNode | None]:
        before_start, last = dummy, dummy
        ctr = 1
        while ctr < left and before_start:
            ctr += 1
            before_start = before_start.next
        last = before_start
        while ctr <= right and last:
            last = last.next
            ctr += 1

        return [before_start, last]

    def reverse_and_return_head_tail(
        self, head: Optional[ListNode]
    ) -> List[ListNode | None]:
        if not head:
            print("head is None")
            return [None]
        prev, cur, tail = None, head, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return [prev, tail]
