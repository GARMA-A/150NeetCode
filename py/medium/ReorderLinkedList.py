from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMiddle(head)
        pre_second_half = mid.next
        mid.next = None
        second_half = self.reverse(pre_second_half)
        first_half = head
        while first_half and second_half:
            first_next = first_half.next
            second_next = second_half.next
            first_half.next = second_half
            second_half.next = first_next
            first_half = first_next
            second_half = second_next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
