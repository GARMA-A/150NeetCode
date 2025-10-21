from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root , root.val)]
        while stack:
            top  ,val= stack.pop()
            if  not top.left and not top.right and val == targetSum :
                return True
            if top.right:
                stack.append((top.right,val+top.right.val))
            if top.left:
                stack.append((top.left , val+top.left.val))
        return False

