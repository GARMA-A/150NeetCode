from typing import List, Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        deq = deque([root])

        while deq:
            level = []
            for _ in range(len(deq)):
                top = deq.popleft()
                level.append(top.val)
                if top.left:
                    deq.append(top.left)

                if top.right:
                    deq.append(top.right)
            ans.append(level)

        return ans


