from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        dummy :ListNode = ListNode(-1)
        if list1.val > list2.val:
            dummy.next = list2
            list2 =list2.next
        else:
            dummy.next = list1
            list1 = list1.next

        dummy_tail = dummy.next

        while list1 and list2:
            if list1.val > list2.val:
                dummy_tail.next = list2
                list2 = list2.next
            else:
                dummy_tail.next = list1
                list1 = list1.next
            dummy_tail = dummy_tail.next

        if  list1 :
            dummy_tail.next = list1
        if  list2:
            dummy_tail.next = list2



        return dummy.next

