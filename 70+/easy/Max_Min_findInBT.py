from collections import deque
from typing import List, Optional

class Node:
    def __init__(self,key:int) -> None:
        self.val :int= key
        self.right :Optional[Node]=None
        self.left :Optional[Node]= None


class Solution:
    def __init__(self) -> None:
        self.mn = float("inf")
        self.mx = float("-inf")

    def find_Min_Max(self,root:Optional[Node])->List[int]:
        if not root:
            return [0,0]
        mn , mx = float("inf") , float("-inf")
        deq  = deque([root])
        while deq:
            top = deq.popleft()
            mn = min(mn , top.val)
            mx = max(mx , top.val)
            if top.left:
                deq.append(top.left)
            if top.right:
                deq.append(top.right)

        return [int(mn),int(mx)]




root = Node(1)
root.left = Node(7)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right.left = Node(5)

s = Solution()

print(s.find_Min_Max(root))

