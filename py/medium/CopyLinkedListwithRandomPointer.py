from re import template
from typing import Optional


class ListNode:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        mp, temp = {}, head
        while temp:
            mp[temp] = ListNode(temp.val)
            temp = temp.next
        temp = head
        while temp:
            mp[temp].next = mp.get(temp.next)
            mp[temp].random = mp.get(temp.random)
            temp = temp.next
        return mp[head]
