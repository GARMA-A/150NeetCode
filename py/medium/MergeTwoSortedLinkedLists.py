from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode()
        if list1.val <= list2.val:
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        temp: ListNode = dummy.next

        while list2 and list1:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1 and not list2:
            temp.next = list1
        if list2 and not list1:
            temp.next = list2

        return dummy.next
