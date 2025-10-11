from typing import Optional

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
        
