from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def __init__(self) -> None:
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def DFS(root:Optional[TreeNode])->int:
            if root is None:
                return 0
            left=DFS(root.left)
            right=DFS(root.right)
            self.diameter = max(self.diameter , left+right)
            return 1+max(left , right)
        DFS(root)
        return self.diameter
