from collections import deque
from typing import Optional 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deq = deque([root])
        ans = 1
        while deq:
            level_size = len(deq)
            for _ in range(level_size):
                top  = deq.popleft()
                if not top.left and not top.right:
                    return ans
                if top.left:
                    deq.append(top.left)
                if top.right:
                    deq.append(top.right)
            ans+=1


        return ans






