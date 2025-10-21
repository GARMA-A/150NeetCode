from typing import Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        max_depth = 0
        if root.left:
            max_depth = max(max_depth , self.maxDepth(root.left))
        if root.right:
            max_depth = max(max_depth  , self.maxDepth(root.right))
        return max_depth+1



class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0
        deq = deque([root])
        while deq:
            for _ in range(len(deq)):
                top  = deq.popleft()
                if top.left:
                    deq.append(top.left)
                if top.right:
                    deq.append(top.right)
            max_depth+=1

        return max_depth
