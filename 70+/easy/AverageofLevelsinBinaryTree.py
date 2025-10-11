from collections import deque
from typing import Optional ,List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        ans = []
        deq =  deque([root])
        while deq:
            sum_of_level = 0
            size = len(deq)
            for _ in range(size):
                top = deq.popleft()
                sum_of_level+=top.val
                if top.right:
                    deq.append(top.right)
                if top.left:
                    deq.append(top.left)
            ans.append(float(sum_of_level/size))



        return ans

