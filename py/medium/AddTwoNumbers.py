from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        dummy = ListNode(0)
        temp = dummy
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if sum > 9:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            temp.next = ListNode(carry)

        return dummy.next
