from collections import deque
from typing import Optional


class Node:
    def __init__(self, key):
        self.left :Optional[Node]= None
        self.right :Optional[Node]= None
        self.val = key

class Solution():
    def printEachLevel(self , root: Optional["Node"]):
        if not root:
            return None
        def BFS():
            dq = deque([root])
            while dq:
                level_size = len(dq)
                level_node = []
                for _ in range(level_size):
                    top = dq.popleft()
                    level_node.append(str(top.val))
                    if top.left:
                        dq.append(top.left)
                    if top.right:
                        dq.append(top.right)
                print(" ".join(level_node))

        BFS()

s = Solution()

root = Node(1)
root.left = Node(7)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right.left = Node(5)



s.printEachLevel(root)




